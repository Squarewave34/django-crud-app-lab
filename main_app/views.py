from django.shortcuts import render, redirect
from django.http import HttpResponse
from main_app.models import Crime
from .forms import VictimsForm
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

class Home(LoginView):
  template_name = 'Home.html'

@login_required
def cases(req):
  crimes = Crime.objects.filter(user=req.user)
  return render(req, 'cases/all-cases.html', {'crimes': crimes})

@login_required
def case_details(req, crime_id):
  crime = Crime.objects.get(id=crime_id)
  victims = VictimsForm()
  return render(req, 'cases/case-details.html', {'crime': crime, 'victims': victims})

class CaseCreate(LoginRequiredMixin, CreateView):
  model = Crime
  fields = ['title', 'location', 'description', 'date', 'open', 'successful', 'responsibility_of']
  def form_valid(self, form):
    form.instance.user = self.request.user 
    return super().form_valid(form)

class CaseUpdate(LoginRequiredMixin, UpdateView):
  model = Crime
  fields = ['title', 'location', 'description', 'date', 'open', 'successful', 'responsibility_of']

class CaseDelete(LoginRequiredMixin, DeleteView):
  model = Crime
  success_url = '/cases/'

@login_required
def add_victim(request, crime_id):
  form = VictimsForm(request.POST)
  # validate the form
  if form.is_valid():
    new_victim= form.save(commit=False)
    new_victim.crime_id = crime_id
    new_victim.save()
  return redirect('case-details', crime_id=crime_id)

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('all-cases')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'signup.html', context)
