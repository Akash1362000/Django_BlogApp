from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect, render
from rest_framework import generics, filters
from rest_framework.response import Response
from rest_framework.views import APIView

from .forms import PostForm
from .models import Post
from .serializer import PostSerializer


def home(request):
    context = {"posts": Post.objects.all()}
    return render(request, "blog/home.html", context)


def about(request):
    return render(request, "blog/about.html", {"title": "About"})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    context = {"post": post}
    return render(request, "blog/post_detail.html", context)


@login_required
def create_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.author = request.user
            user.save()
            messages.success(request, "The post has been created successfully.")
            return redirect("blog-home")
        else:
            messages.error(request, "Please correct the following errors:")
    else:
        form = PostForm()
    return render(request, "blog/create_post.html", {"form": form})


class BlogListView(generics.ListAPIView):
    queryset = Post.objects.all().order_by("-date_posted")
    serializer_class = PostSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'content']  # Các trường cần tìm kiếm

class BlogDetailView(APIView):
    """
        Retrieve, update or delete a snippet instance.
        """

    def get_object(self, slug):
        try:
            return Post.objects.get(slug=slug)
        except Post.DoesNotExist:
            raise Http404

    def get(self, request, slug, format=None):
        snippet = self.get_object(slug)
        serializer = PostSerializer(snippet)
        return Response(data=serializer.data, content_type="application/json")
