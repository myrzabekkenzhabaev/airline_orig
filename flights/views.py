from django.shortcuts import redirect, render, get_object_or_404
from django.shortcuts import render, get_object_or_404
from .models import Flight, Airport, Passenger

def index(request):
    flights = Flight.objects.all()
    airports = Airport.objects.all() 
    return render(request, "flights/index.html", {"flights": flights, "airports":airports})

def flight_detail(request, flight_id):
    flight = get_object_or_404(Flight, pk=flight_id)

    if request.method == "POST":
        new_passenger = {
            'first_name' : request.POST.get('f_name'),
            'email': request.POST.get('email')
        }
        passenger = Passenger.objects.filter(email=new_passenger['email']).first()
        if not passenger:
            passenger = Passenger.objects.create(**new_passenger)
            passenger.flights.add(flight)
        else : 
            passenger.first_name = new_passenger['first_name']
            passenger.save()
            passenger.flights.add(flight)

        if flight.capacity > 0:
            flight.capacity -= 1
            flight.save()

        return redirect("flight_detail", flight_id=flight.id)

    return render(request, "flights/flight_detail.html", {"flight": flight})

def airport_detail(request, airport_id):
    airport = get_object_or_404(Airport, pk=airport_id)
    departures = Flight.objects.filter(origin=airport)
    arrivals = Flight.objects.filter(destination=airport)
    return render(request, "flights/airport_detail.html", {"airport": airport, "departures": departures, "arrivals": arrivals})

def passenger_detail(request):
    email = request.GET.get('email')
    passenger = None
    flights = []

    if email:
        passenger = Passenger.objects.filter(email=email).first()
        if passenger:
            flights = passenger.flights.all()

    return render(request, "flights/my_flights.html", {"passenger": passenger, "flights": flights})