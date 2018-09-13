from django.urls import path
from django.shortcuts import render
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('submit',views.submit, name = 'submit'),
    path('delete/<int:id>',views.delete, name = 'delete'),
    path('archive/<int:id>',views.archive, name = 'archive')
    ]