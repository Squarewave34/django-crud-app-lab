from django.shortcuts import render
from django.http import HttpResponse
from main_app.models import Crime

def home(request):
  crimes = Crime.objects.all()
  return render(request, 'home.html', {'crimes': crimes})

def cases(req):
  crimes = Crime.objects.all()
  return render(req, 'cases/all-cases.html', {'crimes': crimes})

def criminals(req):
  return render(req, 'all-criminals.html')

def case_details(req):
  return render(req, 'case-details.html')

def criminal_details(req):
  return render(req, 'criminal-details.html')
