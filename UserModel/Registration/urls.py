from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.displayy, name='/'),
    path('um', views.register, name='um')
]
