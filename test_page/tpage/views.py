from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author': 'Tikász Zsolt',
        'title': 'Blog post 01',
        'content': 'First content',
        'date_posted': '2022.oktober 16.'
    },
    {
        'author': 'Tikász Zsolt',
        'title': 'Blog post 02',
        'content': '2. content',
        'date_posted': '2022.oktober 17.'
    },
    {
        'author': 'Tikász Zsolt',
        'title': 'Blog post 03',
        'content': 'Asd content',
        'date_posted': '2022.oktober 18.'
    }
]

def fpage(request):
    context = {
        'posts': posts
    }
    return render(request, 'tpage/first.html', context=context)

def secpage(request):
    return render(request, 'tpage/secpage.html')