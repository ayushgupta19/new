from django import views
from django.contrib import admin
from django.urls import path 
from . import views

urlpatterns = [
    path('user/create/',views.showformdata),
    path('form/fields/',views.showdata1),
    path('users/',views.showdata), 
    path('form/fields/<int:user_id>/',views.showdata1),
     path('form/',views.maildata)]