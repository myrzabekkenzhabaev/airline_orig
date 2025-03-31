from django.contrib import admin
from .models import Airport, Flight , Passenger

class AirportAdmin(admin.ModelAdmin):
    list_display = ('code', 'city')
    search_fields = ('code', 'city')
    ordering = ('code', )

class FlightAdmin(admin.ModelAdmin):
    list_display = ('origin', 'destination')
    search_fields = ('origin', 'destination')
    ordering = ('origin', 'destination')

class PassengerAdmin(admin.ModelAdmin):
    list_display = ('email',)
    search_fields = ('email', 'name')
    ordering = ('-id',)
    filter_horizontal = ('flights',)

admin.site.register(Flight, FlightAdmin)
admin.site.register(Airport, AirportAdmin)
admin.site.register(Passenger, PassengerAdmin)