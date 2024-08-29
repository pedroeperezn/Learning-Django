from django.shortcuts import render
from .models import Post
from django.contrib.auth.decorators import login_required

# Create your views here.
def posts_list(request):
    # Store all posts that are stored in the database
    posts = Post.objects.all().order_by('-date')
    # Pass the posts as dictionary to our view
    return render(request,'posts/posts_list.html', {"posts":posts})

def post_page(request, slug):
    # Store all posts that are stored in the database
    post = Post.objects.get(slug=slug)
    # Pass the posts as dictionary to our view
    return render(request,'posts/post_page.html', {"post":post})

# Checks if user is logged in, if not it will redirect to login
@login_required(login_url='/users/login/')
def post_new(request):
    return render(request, 'posts/post_new.html')