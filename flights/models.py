from django.db import models

class Airport(models.Model):
    code = models.CharField(max_length=3, unique=True)
    city = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.city} ({self.code})"

class Flight(models.Model):
    origin = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="departures")
    destination = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="arrivals")
    duration = models.IntegerField()
    capacity = models.IntegerField(default = 50) # type: ignore

    def __str__(self):
        return f"{self.origin} to {self.destination} - {self.duration} min"

class Passenger(models.Model):
    first_name = models.TextField(blank=True, null=True)
    email = models.TextField(blank=True, null=True)
    flights = models.ManyToManyField("Flight", blank=True, related_name="passengers")

    def __str__(self):
            return f"{self.email}"