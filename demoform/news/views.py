from django.http import HttpResponse
from django.shortcuts import render
from .forms import PostForm
# Create your views here.

def index(request):
    return HttpResponse("xin chao")

def add_post(request):
    a = PostForm 
    return render(request,'news/add_news.html',{'f':a})

def save_news(request):
    if request.method == 'POST':
        g = PostForm(request.Post)
        if g.is_valid():
            g.save()
            return HttpResponse('luu')
        else:
            return HttpResponse('khong luu duoc')
    else:
        return HttpResponse('khong phai post request')