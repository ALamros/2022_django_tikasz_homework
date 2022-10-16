from django.urls import path
from .views import fpage, secpage

urlpatterns = [
    path('', fpage, name="blog-fpage"),
    path('secpage', secpage, name="blog-secpage")
]