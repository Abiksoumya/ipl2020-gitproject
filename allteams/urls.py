from django import views
from django.urls import path
from allteams import views

urlpatterns = [
    path('',views.home, name='home'),
    
]