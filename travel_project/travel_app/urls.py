from django.urls import path
from . import views

urlpatterns = [
    path('', views.Welcome.as_view(), name="welcome"),
    path('about/', views.About.as_view(), name="about"),
    path('home/', views.Home.as_view(), name="home"),
    path('trips/', views.TripList.as_view(), name="trip_list"),
    path('trips/new/', views.TripCreate.as_view(), name="trip_create"),
    path('trips/<int:pk>', views.TripDetail.as_view(), name="trip_detail"),
    path('trips/<int:pk>/update',views.TripUpdate.as_view(), name="trip_update"),
    path('trips/<int:pk>/delete',views.TripDelete.as_view(), name="trip_delete"),
    path('list/new/', views.ListCreate.as_view(), name="list_create"),
    path('list/', views.ShowListCategories.as_view(), name="trip_detail"),
]