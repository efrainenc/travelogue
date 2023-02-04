from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Trip(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  destination = models.CharField(max_length=150)
  start_date = models.DateField(blank=True, null=True) # TODO change date forms to show correct format
  end_date = models.DateField(blank=True, null=True)
  created_at = models.DateTimeField(auto_now_add=True)
  
  def __str__(self):
    return self.destination

  class Meta:
    ordering = ['created_at']


class Budget(models.Model):
  PURPOSE_CHOICES = (
    ('Food', 'FOOD'),
    ('Transportation', 'TRANSPORTATION'),
    ('Entertainment', 'ENTERTAINMENT'),
    ('Other', 'OTHER'),
  )
  CURRENCY_CHOICES = (
    ('USD', 'USD'),
    ('CAD', 'CAD'),
    ('EUR', 'EUR'),
    ('JPY', 'JPY'),
    ('GBP', 'GBP'),
    ('AUD', 'AUD'),
  )
  trip = models.ForeignKey(Trip, on_delete=models.CASCADE)
  currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES, default='USD')
  purpose = models.CharField(max_length=30, choices=PURPOSE_CHOICES, default='other')
  budget = models.IntegerField(blank=True, null=True)

  def __str__(self):
    return self.purpose

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