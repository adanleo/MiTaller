# Generated by Django 4.2.7 on 2023-11-14 22:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='document_number',
        ),
        migrations.RemoveField(
            model_name='user',
            name='phone_number',
        ),
    ]