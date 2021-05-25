from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='Blog Home'),
    path('blogpost/<int:pid>', views.blogpost, name='Blog Post'),
]
