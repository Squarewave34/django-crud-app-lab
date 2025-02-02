from django.shortcuts import render, redirect
from django.http import HttpResponse
from main_app.models import Crime
from .forms import VictimsForm
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
  victims = VictimsForm()
  return render(req, 'cases/case-details.html', {'crime': crime, 'victims': victims})

class CaseCreate(CreateView):
  model = Crime
  fields = '__all__'

class CaseUpdate(UpdateView):
  model = Crime
  fields = '__all__'

class CaseDelete(DeleteView):
  model = Crime
  success_url = '/cases/'

def add_victim(request, crime_id):
  form = VictimsForm(request.POST)
  # validate the form
  if form.is_valid():
    new_victim= form.save(commit=False)
    new_victim.crime_id = crime_id
    new_victim.save()
  return redirect('case-details', crime_id=crime_id)