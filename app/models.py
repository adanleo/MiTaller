from django.db import models
from django.contrib.auth.models import User

'''
    Modelos de la tablas de la base de datos
'''


class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    document_number = models.PositiveIntegerField(blank=True)
    phone_number = models.PositiveIntegerField(blank=True)
    admin = models.BooleanField(default=False)
    address = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.user.username}"


class Car(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, default=None)
    license_plate = models.CharField(max_length=9)
    model = models.CharField(max_length=50)
    brand = models.CharField(max_length=50)
    vin = models.CharField(max_length=17)
    motor = models.CharField(max_length=17)

    def __str__(self):
        return f"{self.model}, {self.brand}"
