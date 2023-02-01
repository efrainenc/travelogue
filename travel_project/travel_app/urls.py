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
    path('trips/<int:pk>/list/new/', views.ListCreate.as_view(), name="list_create"),
    path('trips/<int:trip_pk>/list/<int:pk>/update',views.ListUpdate.as_view(), name="list_update"),
    path('trips/<int:trip_pk>/list/<int:pk>/delete',views.ListDelete.as_view(), name="list_delete"),
    path('trips/<int:trip_pk>/list/<int:list_pk>/item/new', views.ItemCreate.as_view(), name="item_create"),
    path('trips/<int:trip_pk>/list/<int:list_pk>/item/<int:pk>/update',views.ItemUpdate.as_view(), name="item_update"),
    path('trips/<int:trip_pk>/list/<int:list_pk>/item/<int:pk>/delete',views.ItemDelete.as_view(), name="item_delete"),
]