"""Определяет схемы URL для learning_logs."""

from django.urls import path, include
from . import views

app_name = 'learning_logs'
urlpatterns = [
    path('', views.index, name='index'),
    #the page with all topics
    path('topics/', views.topics, name='topics'),
]
