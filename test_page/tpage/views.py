from django.shortcuts import render
from .models import PostsModel



def fpage(request):
    posts = PostsModel.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'tpage/first.html', context=context)

def secpage(request):
    return render(request, 'tpage/secpage.html')