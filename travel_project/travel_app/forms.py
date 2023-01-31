from django import forms
from .models import Trip

class DateInput(forms.DateInput):
  input_type = 'date'

class DateForm(forms.Form):
  my_date_field = forms.DateField(widget=DateInput)

class DateModelForm(forms.Form):
  class Meta:
    model = Trip
    fields = '__all__'
    widgets = {'my_date_field' : DateInput()}