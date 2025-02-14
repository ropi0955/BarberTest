from django.contrib import admin
from .models import Barber, Service, Appointment

@admin.register(Barber)
class BarberAdmin(admin.ModelAdmin):
    list_display = ("name", "specialty", "experience")
    search_fields = ("name", "specialty")

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "duration")
    search_fields = ("name",)

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ("user", "barber", "service", "date", "status")
    list_filter = ("status", "barber", "service")
    search_fields = ("user__username", "barber__name", "service__name")
    ordering = ("-date",)
