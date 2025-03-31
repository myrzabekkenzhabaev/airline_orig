from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("flights/<int:flight_id>/", views.flight_detail, name="flight_detail"),
    path("airport_detail/<int:airport_id>/", views.airport_detail, name="airport_detail"),
    path("my_flights/", views.passenger_detail, name="passenger_detail"),
]
