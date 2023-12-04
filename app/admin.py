from django.contrib import admin

from .models import Client, Car, Description

admin.site.register(Client)
admin.site.register(Car)
admin.site.register(Description)
# Register your models here.
