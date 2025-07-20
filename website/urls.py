
from django.urls import path
from website.views import index_view, about_view, contact_view,test_view, newsletter_view

app_name = "website"

urlpatterns = [
    path('home/', index_view, name = 'index'),
    path('about/', about_view, name ='about'),
    path('contact/', contact_view, name = "contact"),
    path('test/', test_view, name = 'test'),
    path('newsletter/', newsletter_view, name = 'newsletter'),
]