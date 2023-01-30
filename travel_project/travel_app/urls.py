from django.urls import path
from . import views

urlpatterns = [
    path('', views.Welcome.as_view(), name="welcome"),
    path('about/', views.About.as_view(), name="about"),
    path('home/', views.Home.as_view(), name="home"),
]