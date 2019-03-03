from django.shortcuts import render
from .models import Blog

def home(request):
    blogs = Blog.objects   # 쿼리셋(quaryset) # method 
    return render(request, 'home.html', {'blogs' : blogs})

    #쿼리셋과 메소드의 형식
    #model.queryset.method