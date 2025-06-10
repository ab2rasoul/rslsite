
from django.urls import path
from website.views import index_view, about_view, products_view

urlpatterns = [
    path('home/', index_view),
    path('about/', about_view),
    path('products/', products_view),
]