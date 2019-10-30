from django.urls import path
from . import views

urlpatterns = [
    path('', views.search, name='home'),
    path('random/', views.random, name='random-trivia'),
    path('listcategory_results/', views.search_results, name ='results'),
    
]