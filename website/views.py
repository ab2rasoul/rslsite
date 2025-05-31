from django.shortcuts import render

from django.http import HttpResponse, JsonResponse

def index_view(request):
    return HttpResponse('<h1>Home page.</h1>')


def about_view(request):
    return HttpResponse({'<h1>About us</h1>'})

def products_view(request):
    return HttpResponse('<h2>Products</h2>')

# Create your views here.
