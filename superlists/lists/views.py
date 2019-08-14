from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home_page(request):
    return HttpResponse("<html><title>To-Do lists</title></html>")

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")