from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def homepage_view(request):
    return HttpResponse("<h1>Hello World</h1>")