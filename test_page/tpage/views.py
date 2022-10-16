from django.shortcuts import render
from django.http import HttpResponse

def fpage(request):
    return render(request, 'tpage/first.html')

def secpage(request):
    return render(request, 'tpage/secpage.html')