from django.shortcuts import render
from django.views.generic import TemplateView, DetailView, CreateView, UpdateView, DeleteView
from .models import Trip, Budget, ListCategory, ListItem
from django.urls import reverse_lazy, reverse
from django.contrib.auth.models import User
# Create your views here.

class Welcome(TemplateView):
  template_name = 'welcome.html'

class Home(TemplateView):
  template_name = 'home.html'

class About(TemplateView):
  template_name = 'about.html'

# Trip Views
class TripList(TemplateView):
  template_name = "trip_list.html"
  
  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context["trips"] = Trip.objects.all()
    return context

class TripCreate(CreateView):
  model = Trip
  fields = ['destination', 'start_date', 'end_date']
  template_name = "trip_create.html"
  success_url = "/trips/"

class TripDisplay(DetailView):
  model = User
  template_name = 'trip_list.html'

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    print(self)
    context["trips"] = Trip.objects.filter(user_id= self.object.id)
    return context

class TripDetail(DetailView):
  model = Trip
  template_name = "trip_detail.html"

class TripUpdate(UpdateView):
  model = Trip
  template_name = "trip_update.html"
  fields = ['destination', 'start_date', 'end_date']
  
  def get_success_url(self):
    return reverse('trip_detail', kwargs={'pk': self.object.pk})


class TripDelete(DeleteView):
  model = Trip
  template_name = "trip_delete.html"
  success_url = "/trips/"