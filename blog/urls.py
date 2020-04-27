from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog_home, name="blog_home"),
    path('post/<slug:slug>/', views.single_post, name="single_post"),
    path('posts/', views.post_list, name="post_list")
]