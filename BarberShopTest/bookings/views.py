from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Barber, Service, Appointment, GalleryImage
from .forms import AppointmentForm

@login_required
def book_appointment(request):
    if request.method == "POST":
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.user = request.user
            appointment.save()
            return redirect("appointment_success")
    else:
        form = AppointmentForm()
    
    return render(request, "bookings/book_appointment.html", {"form": form})

def appointment_success(request):
    return render(request, "bookings/appointment_success.html")

def barbers(request):
    barbers = Barber.objects.all()  # Az összes fodrász lekérése az adatbázisból
    return render(request, "bookings/barbers.html", {"barbers": barbers})

def gallery(request):
    images = GalleryImage.objects.all()
    return render(request, "bookings/gallery.html", {"images": images})  # Képek megjelenítése

def contact(request):
    return render(request, "bookings/contact.html")  # Kapcsolati adatok

def home(request):
    return render(request, "bookings/home.html")

def price(request):
    services = Service.objects.all()
    return render(request, "bookings/price.html", {"services": services})
