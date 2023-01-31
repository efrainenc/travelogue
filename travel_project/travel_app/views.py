from django.shortcuts import render
from django.views.generic import TemplateView, DetailView, CreateView, UpdateView, DeleteView
from .models import Trip, Budget, ListCategory, ListItem
from .forms import DateForm, DateInput, DateModelForm
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

# view current user trips
class TripList(TemplateView):
  model = User
  template_name = "trips/trip_list.html"
  
  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context["trips"] = Trip.objects.filter(user_id= self.request.user.id)
    return context

# set current user on create
class TripCreate(CreateView):
  model = Trip
  fields = ['destination', 'start_date', 'end_date']
  template_name = "trips/trip_create.html"
  success_url = "/trips/"
  # self.request.user.id

class TripDetail(DetailView):
  model = Trip
  template_name = "trips/trip_detail.html"

  def get_queryset(self): # so only current user can view
    return self.model.objects.filter(user=self.request.user)

# check current user on update
class TripUpdate(UpdateView):
  model = Trip
  template_name = "trips/trip_update.html"
  fields = ['destination', 'start_date', 'end_date']

  def get_queryset(self): # so only current user can view
    return self.model.objects.filter(user=self.request.user)
  
  def get_success_url(self):
    return reverse('trip_detail', kwargs={'pk': self.object.pk})

# check current user on delete
class TripDelete(DeleteView):
  model = Trip
  template_name = "trips/trip_delete.html"
  
  def get_queryset(self): # so only current user can view
    return self.model.objects.filter(user=self.request.user)

  success_url = "/trips/"


# 'List' Views

# view all lists
class ShowListCategories(TemplateView):
  medel = Trip
  template_name = "trips/lists/list_show.html"
  
  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context["lists"] = ListCategory.objects.filter(trip_id= self.object.id)
    return context