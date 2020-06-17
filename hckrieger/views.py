from django.shortcuts import render
from posts.models import Post
from about.models import About
from websites.models import Website

def homepage(request):
    post1 = Post.objects.order_by('-date_published').filter(published=True).first()
    post2_4 = Post.objects.order_by('-date_published').filter(published=True).all()[1:5]
    sites = Website.objects.order_by('-id').all()
    return render(request, 'hckrieger/index.html', {'post1': post1, 'post2_4': post2_4, 'sites': sites})

def about(request):
    text = About.objects.first()
    return render(request, 'hckrieger/about.html', {'text': text})
