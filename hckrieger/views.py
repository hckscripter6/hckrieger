from django.shortcuts import render
from posts.models import Post

def homepage(request):
    post1 = Post.objects.filter(published=True).last()
    post2_4 = Post.objects.order_by('-id').filter(published=True).all()[1:5]
    return render(request, 'hckrieger/index.html', {'post1': post1, 'post2_4': post2_4})