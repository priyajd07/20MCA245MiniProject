from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class Register(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    address=models.TextField()
    phone_number = PhoneNumberField()

class Politics(models.Model):
    Politicians=models.TextField()
