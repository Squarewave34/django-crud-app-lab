from django.db import models
# ref: https://www.geeksforgeeks.org/django-model-data-types-and-fields-list/

class Crime(models.Model):
  title = models.CharField(max_length=100)
  location = models.CharField(max_length=100)
  description = models.TextField(max_length=250)
  date = models.DateField()
  victims = models.TextField(max_length=500)
  open = models.BooleanField()
  successful = models.BooleanField()
  responsibility_of = models.CharField(max_length=100)

  def __str__(self):
    return self.title