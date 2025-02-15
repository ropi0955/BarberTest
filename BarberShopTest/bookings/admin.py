from django.contrib import admin
from .models import Barber, Service, Appointment, GalleryImage

@admin.register(Barber)
class BarberAdmin(admin.ModelAdmin):
    list_display = ("name", "specialty", "experience")
    search_fields = ("name", "specialty")
    list_filter = ("specialty",)
    readonly_fields = ("profile_image_preview",)

    def profile_image_preview(self, obj):
        if obj.profile_image:
            return f'<img src="{obj.profile_image.url}" width="100" height="100" style="border-radius:50%"/>'
        return "Nincs kép"
    profile_image_preview.allow_tags = True
    profile_image_preview.short_description = "Profilkép"

@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ("description", "uploaded_at")
    search_fields = ("description",)

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
