from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    # This posts_list method is the one we already declared
    # In our views.py file. It will call that view. 
    path('register/', views.register_user, name='register_user'),
    # User login URL
    path('login/', views.login_user, name='login_user'),
    # User log out 
    path('logout/', views.logout_user, name='logout_user'),
]