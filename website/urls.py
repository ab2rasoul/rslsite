
from django.urls import path
from website.views import index_view, about_view, contact_view

app_name = "website"

urlpatterns = [
    path('index/', index_view),
    path('about/', about_view),
    path('contact/', contact_view),
]