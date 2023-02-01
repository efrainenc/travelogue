from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Trip(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  destination = models.CharField(max_length=150)
  start_date = models.DateField(blank=True, null=True)
  end_date = models.DateField(blank=True, null=True)
  created_at = models.DateTimeField(auto_now_add=True)
  
  def __str__(self):
    return self.destination

  class Meta:
    ordering = ['created_at']


class Budget(models.Model):
  trip = models.ForeignKey(Trip, on_delete=models.CASCADE)
  user_currency = models.CharField(max_length=3)
  trip_currency = models.CharField(max_length=3, blank=True, null=True)
  budget = models.IntegerField(blank=True, null=True)

  def __str__(self):
    return self.name

class ListCategory(models.Model):
  trip = models.ForeignKey(Trip, on_delete=models.CASCADE)
  category = models.CharField(max_length=100)

  def __str__(self):
    return self.category

  class Meta:
    ordering = ['category']

class ListItem(models.Model):
  category = models.ForeignKey(ListCategory, on_delete=models.CASCADE)
  list_item = models.CharField(max_length=500, blank=True, null=True)

  def __str__(self):
    return self.list_item

  class Meta:
    ordering = ['category']