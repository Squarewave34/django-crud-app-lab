from django import forms
from .models import Victim

class VictimsForm(forms.ModelForm):
  class Meta:
    model = Victim
    fields = ['name', 'age']
