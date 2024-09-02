from django.shortcuts import render, redirect
from .models import Post
from django.contrib.auth.decorators import login_required
# import forms for adding new posts with our forms.py file
from . import forms

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
# This page will allow users adding new posts. This functionality will only be available on login
@login_required(login_url='/users/login/')
def post_new(request):
    # Check if there's a post submission (the method is post)
    if request.method == 'POST':
        # Create a post with the request as parameter and the files that were passed in the form
        form = forms.CreatePost(request.POST, request.FILES)
        # Validate form agains model
        if form.is_valid():
            # Save with user
            newpost = form.save(commit=False)
            newpost.author = request.user
            newpost.save()
            # Redirect to the posts list
            return redirect('posts:list')
            
    # If not, then show the empty form
    else:
        form = forms.CreatePost()
    # If login is succesfull, we return the form that we created in forms.py
    return render(request, 'posts/post_new.html', {"form":form})

