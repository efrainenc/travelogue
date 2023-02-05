from django import forms
from .models import Trip, Budget, ListCategory, ListItem

class DateForm(forms.ModelForm):
  start_date = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}))
  end_date = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}))

  class Meta:
    model = Trip
    fields = ['destination', 'start_date', 'end_date']

class ContactForm(forms.Form):
  name = forms.CharField(max_length=100)
  email = forms.EmailField()
  subject = forms.CharField(max_length=100)
  message = forms.CharField(widget=forms.Textarea)
