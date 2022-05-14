from django.urls import path
from . import views

urlpatterns = [
    path("", views.Home.as_view(), name="blog-home"),
    path("about/", views.About.as_view(), name="blog-about"),
    path("posts/<int:pk>", views.GetPost.as_view(), name="get_post"),
    path("posts/create", views.CreatePost.as_view(), name="create_post"),
    path("posts/<int:pk>/delete", views.DeletePost.as_view(), name="delete_post"),
    path("posts/<int:pk>/update", views.UpdatePost.as_view(), name="update_post"),
]
