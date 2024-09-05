from django.urls import path
from . import views

# This indicates that the current URLs are inside of the application named posts
app_name = 'posts'

urlpatterns = [
    # Changed link to be name='posts'
    path('', views.posts_list, name='list'),
    # This link will add a new post, needs to be before the slug
    path('new-post/', views.post_new, name='new-post'),
    # This will receive an slug and will generate a posts_page in the views
    path('<slug:slug>', views.post_page, name='page'),
]