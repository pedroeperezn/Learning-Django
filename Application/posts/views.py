from django.shortcuts import render
from .models import Post


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
    