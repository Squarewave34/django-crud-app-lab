from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  # cases / crimes
  path('cases/', views.cases, name='all-cases'),
  path('cases/<int:crime_id>', views.case_details, name='case-details'),
  path('cases/create/', views.CaseCreate.as_view(), name='case-create'),
  path('cases/<int:pk>/update/', views.CaseUpdate.as_view(), name='case-update'),
  path('cases/<int:pk>/delete/', views.CaseDelete.as_view() ,name='case-delete'),

  path('criminals/', views.criminals, name='all-criminals'),
  path('criminal/', views.criminal_details, name='criminal-details'),
]