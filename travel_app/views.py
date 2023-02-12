from django.shortcuts import render, redirect
from django.views.generic import TemplateView, DetailView, CreateView, UpdateView, DeleteView
from .models import Trip, Budget, ListCategory, ListItem
from .forms import DateForm, ContactForm
from django.urls import reverse_lazy, reverse
from django.contrib.auth.models import User
import requests
from django.core.mail import send_mail


# Create your views here.
class Home(TemplateView):
  template_name = 'home.html'

class Contact(TemplateView):
  template_name = 'contact.html'

  def contact_us(request):
    if request.method == 'POST':
      form = ContactForm(request.POST)
      if form.is_valid():
        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        subject = form.cleaned_data['subject']
        message = form.cleaned_data['message']
        send_mail(subject, message, email, ['efraine387@gmail.com'], fail_silently=False)
        return redirect('home')
    else:
      form = ContactForm()
    return render(request, 'contact.html', {'form': form})

# Trip Views

# view current user trips
class TripList(TemplateView):
  model = User
  template_name = "trips/trip_list.html"
  
  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context["trips"] = Trip.objects.filter(user_id= self.request.user.id)
    return context

class TripCreate(CreateView):
  model = Trip
  form_class = DateForm
  template_name = "trips/trip_create.html"
  success_url = "/trips/"

  def form_valid(self, form):
    form.instance.user_id = self.request.user.id
    return super().form_valid(form)

class TripDetail(DetailView): # TODO ADD THE WEATHER API AND GOOGLE CALENDAR
  model = Trip
  template_name = "trips/trip_detail.html" 

  # view lists from trip detail
  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context["budgets"] = Budget.objects.filter(trip_id= self.object.id)
    context["lists"] = ListCategory.objects.filter(trip_id= self.object.id)
    context["items"] = ListItem.objects.all()
    # ^^ not very scalable, becomes issue to loop though all items 
    # of all users, maybe add trip fk to items
    return context

  def get_queryset(self): # so only current user can view
    return self.model.objects.filter(user=self.request.user)
  

class TripUpdate(UpdateView):
  model = Trip
  form_class = DateForm
  template_name = "trips/trip_update.html"

  def get_queryset(self): # so only current user can view
    return self.model.objects.filter(user=self.request.user)
  
  def get_success_url(self):
    return reverse('trip_detail', kwargs={'pk': self.kwargs['pk']})

class TripDelete(DeleteView):
  model = Trip
  template_name = "trips/trip_delete.html"
  success_url = "/trips/"

  def get_queryset(self): # so only current user can view
    return self.model.objects.filter(user=self.request.user)


# 'List' Views
class ListCreate(CreateView):
  model = ListCategory
  fields = ['category']
  template_name = "trips/lists/list_create.html"
  
  def get_success_url(self):
    return reverse('trip_detail', kwargs={'pk': self.kwargs['pk']})

  def form_valid(self, form):
    form.instance.trip_id = self.kwargs['pk']
    return super().form_valid(form)

class ListUpdate(UpdateView):
  model = ListCategory
  template_name = "trips/lists/list_update.html"
  fields = ['category']

  def get_success_url(self):
    return reverse('trip_detail', kwargs={'pk': self.kwargs['trip_pk']})

  def get_queryset(self): # so only current trip can view
    return self.model.objects.filter(trip_id= self.kwargs['trip_pk'])

class ListDelete(DeleteView):
  model = ListCategory
  template_name = "trips/lists/list_delete.html"

  def get_success_url(self):
    return reverse('trip_detail', kwargs={'pk': self.kwargs['trip_pk']})

  def get_queryset(self): # so only current trip can view
    return self.model.objects.filter(trip_id= self.kwargs['trip_pk'])


# 'Item' Views

class ItemCreate(CreateView):
  model = ListItem
  fields = ['list_item']
  template_name = "trips/lists/items/item_create.html"

  def get_success_url(self):
    return reverse('trip_detail', kwargs={'pk': self.kwargs['trip_pk']})

  # def get_queryset(self): # so only current list can view
  #   return self.model.objects.filter(category_id= self.kwargs['item_pk'])
  
  def form_valid(self, form):
    form.instance.category_id = self.kwargs['list_pk']
    return super().form_valid(form)

class ItemUpdate(UpdateView):
  model = ListItem
  template_name = "trips/lists/items/item_update.html"
  fields = ['list_item']

  def get_success_url(self):
    return reverse('trip_detail', kwargs={'pk': self.kwargs['trip_pk']})

  # def get_queryset(self): # so only current list can view
  #   return self.model.objects.filter(category_id= self.kwargs['item_pk'])

class ItemDelete(DeleteView):
  model = ListItem
  template_name = "trips/lists/items/item_delete.html"

  def get_success_url(self):
    return reverse('trip_detail', kwargs={'pk': self.kwargs['trip_pk']})

  # def get_queryset(self): # so only current list can view
  #   return self.model.objects.filter(category_id= self.kwargs['list_pk'])


# 'Budget' Views
class BudgetCreate(CreateView):
  model = Budget
  fields = ['purpose','currency', 'budget']
  template_name = "trips/budgets/budget_create.html"

  def get_success_url(self):
    return reverse('trip_detail', kwargs={'pk': self.kwargs['pk']})

  def form_valid(self, form):
    form.instance.trip_id = self.kwargs['pk']
    return super().form_valid(form)

class BudgetUpdate(UpdateView):
  model = Budget
  template_name = "trips/budgets/budget_update.html"
  fields = ['purpose','currency', 'budget']

  def get_success_url(self):
    return reverse('trip_detail', kwargs={'pk': self.kwargs['trip_pk']})

  def get_queryset(self): # so only current trip can view
    return self.model.objects.filter(trip_id= self.kwargs['trip_pk'])

class BudgetDelete(DeleteView):
  model = Budget
  template_name = "trips/budgets/budget_delete.html"

  def get_success_url(self):
    return reverse('trip_detail', kwargs={'pk': self.kwargs['trip_pk']})

  def get_queryset(self): # so only current trip can view
    return self.model.objects.filter(trip_id= self.kwargs['trip_pk'])
