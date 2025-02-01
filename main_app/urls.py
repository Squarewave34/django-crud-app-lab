from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('cases/', views.cases, name='all-cases'),
  path('criminals/', views.criminals, name='all-criminals'),
  path('case/', views.case_details, name='case-details'),
  path('criminal/', views.criminal_details, name='criminal-details'),
]