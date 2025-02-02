from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
# ref: https://www.geeksforgeeks.org/django-model-data-types-and-fields-list/

class Crime(models.Model):
  title = models.CharField(max_length=100)
  location = models.CharField(max_length=100)
  description = models.TextField(max_length=250)
  date = models.DateField()
  open = models.BooleanField()
  successful = models.BooleanField()
  responsibility_of = models.CharField(max_length=100)
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return self.title
  
  def get_absolute_url(self):
    # Use the 'reverse' function to dynamically find the URL for viewing this cat's details
    return reverse('case-details', kwargs={'crime_id': self.id})
  

class Victim(models.Model):
  name = models.CharField(max_length=100)
  age = models.IntegerField()

  crime = models.ForeignKey(Crime, on_delete=models.CASCADE)

  def __str__(self):
    return self.name