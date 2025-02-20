from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Barber, Service, Appointment, GalleryImage
from .forms import AppointmentForm
from django.core.mail import send_mail, EmailMessage
from django.conf import settings
from django.template.loader import render_to_string
from .utils import create_calendar_event

@login_required
def book_appointment(request):
    if request.method == "POST":
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.user = request.user
            appointment.save()

            message = render_to_string("bookings/email_template.txt", {
            "user": request.user,
            "appointment": appointment,
        })

            ics_file_path = create_calendar_event(appointment)

            email = EmailMessage(
                subject="Foglalás visszaigazolása - BarberShop",
                body=message,
                from_email=settings.EMAIL_HOST_USER,
                to=[request.user.email],
            )
            email.attach_file(ics_file_path)
            email.send()

            return redirect("appointment_success")
    else:
        form = AppointmentForm()
    
    return render(request, "bookings/book_appointment.html", {"form": form})

def appointment_success(request):
    return render(request, "bookings/appointment_success.html")

def barbers(request):
    barbers = Barber.objects.all()
    return render(request, "bookings/barbers.html", {"barbers": barbers})

def barber_detail(request, barber_id):
    barber = get_object_or_404(Barber, id=barber_id)
    return render(request, "bookings/barber_detail.html", {"barber": barber})

def gallery(request):
    images = GalleryImage.objects.all()
    return render(request, "bookings/gallery.html", {"images": images})

def contact(request):
    return render(request, "bookings/contact.html")

def home(request):
    return render(request, "bookings/home.html")

def price(request):
    services = Service.objects.all()
    return render(request, "bookings/price.html", {"services": services})
