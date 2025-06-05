from django.shortcuts import render

from django.http import HttpResponse, JsonResponse

def index_view(request):
    return render(request,'website/home.html')


def about_view(request):
    return render(request,'website/about.html')

def products_view(request):
    return render(request,'website/products.html')

# Create your views here.
