from django.db import models
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Custom User Manager
class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError("Users must have an email address")
        user = self.model(email=self.normalize_email(email))
        user.password = make_password(password)  # Proper password hashing
        user.save(using=self._db)
        return user

# Custom User Model
class User(AbstractBaseUser):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    objects = UserManager()
    
    USERNAME_FIELD = 'email'

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)  

# Patient Model
class Patient(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

# Heart Rate Model
class HeartRate(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    heart_rate = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)
