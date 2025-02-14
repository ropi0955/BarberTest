from django.urls import path
from .views import appointment_success, book_appointment

urlpatterns = [
    path("book/", book_appointment, name="book_appointment"),
    path("success/", appointment_success, name="appointment_success"),

]
