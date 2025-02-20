from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import UserRegistrationForm
from django.contrib.auth.decorators import login_required
from bookings.models import Appointment

def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data["password"])
            user.save()
            login(request, user)
            return redirect("book_appointment")
    else:
        form = UserRegistrationForm()
    return render(request, "authentication/register.html", {"form": form})

@login_required
def profile(request):
    appointments = Appointment.objects.filter(user=request.user).order_by("-date")
    return render(request, "authentication/profile.html", {"appointments": appointments})

def home(request):
    return render(request, "bookings/home.html")