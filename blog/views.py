from django.shortcuts import render
from posts.models import Post
# Create your views here.

def blog_home(request):
    posts = Post.objects.filter(published=True).order_by('-id').all()[0:5]
    return render(request, 'blog/blog_home.html', {'posts': posts})

def single_post(request, slug):
    post = Post.objects.filter(published=True).get(slug=slug)
    return render(request, 'blog/single_post.html', {'post': post})

def post_list(request):
    posts = Post.objects.filter(published=True).order_by('-id').all
    return render(request, 'blog/posts.html', {'posts': posts})

