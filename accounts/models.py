from django.db import models
from phone_field import PhoneField
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = PhoneField(blank=True, help_text='Contact phone number')