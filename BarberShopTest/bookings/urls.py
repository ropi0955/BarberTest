from django.urls import path
from .views import appointment_success, book_appointment, barbers, gallery, contact, home

urlpatterns = [
    path("", home, name="home"),
    path("book/", book_appointment, name="book_appointment"),
    path("success/", appointment_success, name="appointment_success"),
    path("barbers/", barbers, name="barbers"),
    path("gallery/", gallery, name="gallery"),
    path("contact/", contact, name="contact"),

]
