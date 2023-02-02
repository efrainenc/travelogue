from django import forms
from .models import Trip, Budget, ListCategory, ListItem

class DateInput(forms.DateInput):
  input_type = 'date'

class DateForm(forms.Form):
  my_date_field = forms.DateField(widget=DateInput)

class DateModelForm(forms.Form):
  class Meta:
    model = Trip
    fields = '__all__'
    widgets = {'my_date_field' : DateInput()}

class APIForm(forms.Form):
  destination = forms.CharField(label='City, State/Country..')
  start_date = forms.DateField(label='yyyy-mm-dd')
  end_date = forms.DateField(label='yyyy-mm-dd')


# class YourModelForm(forms.ModelForm):
#     class Meta:
#         model = Trip
#         fields = ['field1', 'field2', ... ]
#         widgets = {
#             'user_id': forms.HiddenInput(),
#         }

# def your_view(request):
#     if request.method == 'POST':
#         form = YourModelForm(request.POST)
#         if form.is_valid():
#             form.instance.user = request.user
#             form.save()
#             # do something
#     else:
#         form = YourModelForm()
    
#     return render(request, 'template.html', {'form': form})