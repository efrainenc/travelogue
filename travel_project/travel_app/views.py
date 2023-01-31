from django.shortcuts import render
from django.views.generic import TemplateView, DetailView, CreateView, UpdateView, DeleteView

# Create your views here.

class Welcome(TemplateView):
  template_name = 'welcome.html'

class Home(TemplateView):
  template_name = 'home.html'

class About(TemplateView):
  template_name = 'about.html'


