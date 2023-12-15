from django.shortcuts import render, redirect
from .models import BlogPost

def create_post(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        date = request.POST['date']
        BlogPost.objects.create(title=title, content=content, date=date)
        return redirect('show_posts')
    return render(request, 'create_post.html')

def show_posts(request):
    posts = BlogPost.objects.all()
    return render(request, 'show_posts.html', {'posts': posts})