from django.shortcuts import render
from django.http import HttpResponse

def fpage(request):
    return HttpResponse('<h1> Page home valami </h1>')

def secpage(request):
    return HttpResponse('<h1> Egyeb oldal </h1>')