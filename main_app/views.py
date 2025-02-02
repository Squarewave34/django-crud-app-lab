from django.shortcuts import render
from django.http import HttpResponse
from main_app.models import Crime
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

def home(request):
  crimes = Crime.objects.all()
  return render(request, 'home.html', {'crimes': crimes})

def cases(req):
  crimes = Crime.objects.all()
  return render(req, 'cases/all-cases.html', {'crimes': crimes})

def case_details(req, crime_id):
  crime = Crime.objects.get(id=crime_id)
  return render(req, 'cases/case-details.html', {'crime': crime})

class CaseCreate(CreateView):
  model = Crime
  fields = '__all__'

class CaseUpdate(UpdateView):
  model = Crime
  fields = '__all__'

class CaseDelete(DeleteView):
  model = Crime
  success_url = '/cases/'


def criminals(req):
  return render(req, 'all-criminals.html')

def criminal_details(req):
  return render(req, 'criminal-details.html')
