from django.urls import path
from .views import fpage, secpage

urlpatterns = [
    path('', fpage, name="blog-home"),
    path('secpage', secpage, name="blog-about")
]