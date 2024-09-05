# Imports render to render HTML templates and redirect for user registration
from django.shortcuts import render, redirect
from django.http import HttpResponse
# Import the user creation form template that is native to django
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

# Create your views here.
def register_user(request):
    # If this page receives a POST request, it is a user's registration, therefore we need to check what was posted
    if request.method == 'POST':
        # Unwrapp the information that was sent
        form = UserCreationForm(request.POST)
        # If the form is valid, save the user
        if form.is_valid():
            # Update to automatically login the user after login. 
            login(request,form.save())
            # If login was succesful, we redirect the user to the posts page
            return redirect('posts:list')
    # Here, we are handling the case in which a request hasn't been sent, it will just pass a regular form
    else:
        form = UserCreationForm()
    # If the form is not valid, it will pass the invalid form and notify the error in the application (existing user, etc.). 
    # Create an instance of a user creation form
    # Look for the view that correspond to this application
    # return HttpResponse("Hello, Django!")
    # Pass the form as context to our page's rendering
    return render(request,'users/register_user.html',{'form':form})

def login_user(request):
    # Check the type of request:
    # If its a post request, then we redirect to user's login
    if request.method == 'POST':
        # We are receiving the data that was sent and we validate it
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            # Successful login
            # Return user
            login(request, form.get_user())
            # If the user tried to access the new page and was redirected to login, then after login
            # they will be redirected to the new post page
            if "next" in request.POST:
                return redirect(request.POST.get("next"))
            else:
                return redirect('posts:list')
        
    # GET request, this is the first time that the user will be requesting to login
    else:
        form = AuthenticationForm()
    return render(request, "users/login.html", {'form':form})
    
def logout_user(request):
    # If the request is a post request, logout
    if request.method == 'POST':
        # logout and redirect to the post list page
        logout(request)
        return redirect('posts:list')
    