from django.http import HttpResponse
from django.shortcuts import render
def homepage(request):
    #return HttpResponse('Hello, world. You\'re at the homepage!')
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')