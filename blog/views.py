from django.http import Http404, HttpResponse
from django.shortcuts import render
from django.urls import reverse

from django.views import View
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    CreateView,
    DetailView,
    DeleteView,
    UpdateView,
    ListView,
)


class Home(ListView):
    template_name = "blog/home.html"
    model = Post
    context_object_name = "posts"
    ordering = "-date_posted"


class About(View):
    def get(self, request):
        return render(request, "blog/about.html", {"title": "About"})


class GetPost(DetailView):
    model = Post
    template_name = "blog/get_post.html"
    context_object_name = "post"


class CreatePost(LoginRequiredMixin, CreateView):
    model = Post
    template_name = "blog/create_post.html"
    fields = ["title", "content"]
    # TODO Don't Hard Code it
    success_url = "/"

    def form_valid(self, form) -> HttpResponse:
        if self.request.user:
            form.instance.author = self.request.user
            return super().form_valid(form)
        # User Not Auth


class UpdatePost(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    template_name = "blog/update_post.html"
    fields = ["title", "content"]

    def test_func(self) -> bool:
        post: Post = self.get_object()
        return post.author == self.request.user


class DeletePost(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = "blog/delete_post.html"
    success_url = "/"

    def test_func(self) -> bool:
        post: Post = self.get_object()
        return post.author == self.request.user
