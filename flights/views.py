from django.shortcuts import render, get_object_or_404
from django.shortcuts import render, get_object_or_404
from .models import Flight, Airport

def index(request):
    flights = Flight.objects.all()
    airports = Airport.objects.all()
    return render(request, "flights/index.html", {"flights": flights, "airports":airports})

def flight_detail(request, flight_id):
    flight = get_object_or_404(Flight, pk=flight_id)
    return render(request, "flights/flight_detail.html", {"flight": flight})

def airport_detail(request, airport_id):
    airport = get_object_or_404(Airport, pk=airport_id)
    return render(request, "flights/airport_detail.html", {"airport": airport})
