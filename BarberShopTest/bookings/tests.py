from django.test import TestCase
from .models import Barber

class BarberModelTest(TestCase):
    def setUp(self):
        self.barber = Barber.objects.create(
            name="John Doe",
            specialty="Fade Haircuts",
            experience=5,
            bio="Professional barber with 5 years of experience.",
        )
    
    def test_barber_creation(self):
        """Test if the Barber instance is created correctly"""
        self.assertEqual(self.barber.name, "John Doe")
        self.assertEqual(self.barber.specialty, "Fade Haircuts")
        self.assertEqual(self.barber.experience, 5)
        self.assertEqual(self.barber.bio, "Professional barber with 5 years of experience.")

    def test_barber_str_representation(self):
        """Test the string representation of the Barber model"""
        self.assertEqual(str(self.barber), "John Doe")