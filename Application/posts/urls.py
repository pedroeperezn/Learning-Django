from django.urls import path
from . import views

# This indicates that the current URLs are inside of the application named posts
app_name = 'posts'

urlpatterns = [
    # Changed link to be name='posts'
    path('', views.posts_list, name='list'),
    # This will receive an slug and will generate a posts_page in the views
    path('<slug:slug>', views.post_page, name='page'),
]