from django.shortcuts import render

from django.http import HttpResponse, JsonResponse

def index_view(request):
    return render(request,'home.html')


def about_view(request):
    return render(request,'about.html')

def products_view(request):
    return render(request,'products.html')

# Create your views here.
