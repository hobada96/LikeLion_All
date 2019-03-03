from django.shortcuts import render

# Create your views here.

def home(requset):
    return render(request, 'home.html')