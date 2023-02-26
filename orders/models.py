from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from Center.models import Service
# Create your models here.

class phoneorder(models.Model):
    phone = PhoneNumberField()

    def __str__(self):
        return self.phone

class orderwork(models.Model):
    service = models.ForeignKey(Service,on_delete=models.CASCADE, blank=True,null=True)
    email = models.EmailField(blank=True)
    phone_number = PhoneNumberField()
    text = models.TextField()

    def __str__(self):
        return f'{self.service} - {self.phone_number}'