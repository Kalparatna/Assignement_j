from django.test import TestCase
from django.contrib.auth.hashers import make_password, check_password
from .models import User, Patient, HeartRate

class UserModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            email="test@example.com",
            password=make_password("password123")  # Hash the password
        )

    def test_create_user(self):
        user = User.objects.get(email="test@example.com")
        self.assertEqual(user.email, "test@example.com")

    def test_password_hashing(self):
        user = User.objects.get(email="test@example.com")
        self.assertTrue(check_password("password123", user.password))  # This should now pass

class PatientModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(email="patient@example.com", password=make_password("password123"))
        self.patient = Patient.objects.create(name="John Doe", age=30, user=self.user)

    def test_create_patient(self):
        patient = Patient.objects.get(name="John Doe")
        self.assertEqual(patient.age, 30)
        self.assertEqual(patient.user.email, "patient@example.com")

class HeartRateModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(email="patient@example.com", password=make_password("password123"))
        self.patient = Patient.objects.create(name="John Doe", age=30, user=self.user)
        self.heart_rate = HeartRate.objects.create(patient=self.patient, heart_rate=75)

    def test_create_heart_rate(self):
        heart_rate = HeartRate.objects.get(patient=self.patient)
        self.assertEqual(heart_rate.heart_rate, 75)
