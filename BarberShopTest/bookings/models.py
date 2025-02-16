from django.db import models
from django.contrib.auth.models import User

class Barber(models.Model):
    name = models.CharField(max_length=100)
    specialty = models.CharField(max_length=200)
    experience = models.IntegerField()
    profile_image = models.ImageField(upload_to="barbers/", blank=True, null=True)

    def __str__(self):
        return self.name

class Service(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    duration = models.IntegerField(help_text="Duration in minutes")

    def __str__(self):
        return self.name

class Appointment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    barber = models.ForeignKey(Barber, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    date = models.DateTimeField()
    status = models.CharField(
        max_length=20,
        choices=[("pending", "Pending"), ("confirmed", "Confirmed"), ("canceled", "Canceled")],
        default="pending"
    )

    def __str__(self):
        return f"{self.user.username} - {self.service.name} - {self.date}"
    
class GalleryImage(models.Model):
    image = models.ImageField(upload_to="gallery/")
    description = models.CharField(max_length=255, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.description if self.description else f"Kép {self.uploaded_at}"
