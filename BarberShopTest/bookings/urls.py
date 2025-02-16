from django.urls import path
from .views import appointment_success, book_appointment, barbers, gallery, contact, home, price, barber_detail

urlpatterns = [
    path("", home, name="home"),
    path("book/", book_appointment, name="book_appointment"),
    path("success/", appointment_success, name="appointment_success"),
    path("barbers/", barbers, name="barbers"),
    path("barbers/<int:barber_id>/", barber_detail, name="barber_detail"),
    path("gallery/", gallery, name="gallery"),
    path("contact/", contact, name="contact"),
    path("price/", price, name="price")
]
