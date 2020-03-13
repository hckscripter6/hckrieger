from django.shortcuts import render
from posts.models import Post
from about.models import About

def homepage(request):
    post1 = Post.objects.filter(published=True).last()
    post2_4 = Post.objects.order_by('-id').filter(published=True).all()[1:5]
    return render(request, 'hckrieger/index.html', {'post1': post1, 'post2_4': post2_4})

def about(request):
    text = About.objects.first()
    return render(request, 'hckrieger/about.html', {'text': text})