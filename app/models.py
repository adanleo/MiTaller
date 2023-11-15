from django.db import models


class User(models.Model):
    name = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    document_number = models.IntegerField(default=0)
    phone_number = models.IntegerField(default=0)
    admin = models.BooleanField(default=False)
    address = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    mail = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name} {self.lastname}"


class Car(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    license_plate = models.CharField(max_length=9)
    model = models.CharField(max_length=50)
    brand = models.CharField(max_length=50)
    vin = models.CharField(max_length=17)
    motor = models.CharField(max_length=17)

    def __str__(self):
        return f"{self.model}, {self.brand}"
