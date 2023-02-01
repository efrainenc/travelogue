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

  def form_valid(self, form):
    form.instance.user_id = self.request.user.id
    return super().form_valid(form)

class TripDetail(DetailView):
  model = Trip
  template_name = "trips/trip_detail.html" 

  # view lists from trip detail
  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context["lists"] = ListCategory.objects.filter(trip_id= self.object.id)
    context["budgets"] = Budget.objects.filter(trip_id= self.object.id)
    context["items"] = ListItem.objects.all()
    # ^^ not very scalable, becomes issue to loop though all items of all users, maybe add user field to li
    # ids = [obj.id for obj in context['lists']]
    # print(f'ALL ids:{ids}')
    #print(f'each id:{id}')
    return context

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

class ListCreate(CreateView):
  model = ListCategory
  fields = ['category']
  template_name = "trips/lists/list_create.html"
  success_url = "/trips/"

  def form_valid(self, form):
    form.instance.trip_id = self.kwargs['pk']
    return super().form_valid(form)

class ListUpdate(UpdateView):
  model = ListCategory
  template_name = "trips/lists/list_update.html"
  fields = ['category']
  success_url = "/trips/"

  def get_queryset(self): # so only current trip can view
    return self.model.objects.filter(trip_id= self.kwargs['trip_pk'])

class ListDelete(DeleteView):
  model = ListCategory
  template_name = "trips/lists/list_delete.html"
  success_url = "/trips/"

  def get_queryset(self): # so only current trip can view
    return self.model.objects.filter(trip_id= self.kwargs['trip_pk'])


# 'Item' Views

class ItemCreate(CreateView):
  model = ListItem
  fields = ['list_item']
  template_name = "trips/lists/items/item_create.html"
  success_url = "/trips/"

  # def get_queryset(self): # so only current list can view
  #   return self.model.objects.filter(category_id= self.kwargs['item_pk'])
  
  def form_valid(self, form):
    form.instance.category_id = self.kwargs['list_pk']
    return super().form_valid(form)

class ItemUpdate(UpdateView):
  model = ListItem
  template_name = "trips/lists/items/item_update.html"
  fields = ['list_item']
  success_url = "/trips/"

  # def get_queryset(self): # so only current list can view
  #   return self.model.objects.filter(category_id= self.kwargs['item_pk'])

class ItemDelete(DeleteView):
  model = ListItem
  template_name = "trips/lists/items/item_delete.html"
  success_url = "/trips/"

  # def get_queryset(self): # so only current list can view
  #   return self.model.objects.filter(category_id= self.kwargs['list_pk'])




# 'Budget' Views
class BudgetCreate(CreateView):
  model = Budget
  fields = ['user_currency', 'trip_currency', 'budget']
  template_name = "trips/budgets/budget_create.html"
  success_url = "/trips/"

  def form_valid(self, form):
    form.instance.trip_id = self.kwargs['pk']
    return super().form_valid(form)

class BudgetUpdate(UpdateView):
  model = Budget
  template_name = "trips/budgets/budget_update.html"
  fields = ['user_currency', 'trip_currency', 'budget']
  success_url = "/trips/"

  def get_queryset(self): # so only current trip can view
    return self.model.objects.filter(trip_id= self.kwargs['trip_pk'])

class BudgetDelete(DeleteView):
  model = Budget
  template_name = "trips/budgets/budget_delete.html"
  success_url = "/trips/"

  def get_queryset(self): # so only current trip can view
    return self.model.objects.filter(trip_id= self.kwargs['trip_pk'])