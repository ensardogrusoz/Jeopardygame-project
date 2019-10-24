from django.urls import path
from . import views

urlpatterns = [
    path('', views.category, name='home'),
    path('random/', views.random, name='random-trivia')
]