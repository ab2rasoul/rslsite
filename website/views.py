from django.shortcuts import render

from django.http import HttpResponse, JsonResponse
from website.models import Contact

def index_view(request):
    return render(request,'website/index.html')


def about_view(request):
    return render(request,'website/about.html')

def contact_view(request):
    return render(request,'website/contact.html')


def test_view(request):
    if request.method == "POST" :
       name = request.POST.get("name")
       email = request.POST.get("email")
       subject = request.POST.get("subject")
       message = request.POST.get("message")
       print(name, email, subject, message)
       c = Contact()
       c.name = name
       c.email = email
       c.subject = subject
       c.message = message
       c.save()
    return render(request, "test.html", {})
# Create your views here.
