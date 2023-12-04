# Generated by Django 4.2.7 on 2023-12-01 19:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('license_plate', models.CharField(max_length=9)),
                ('model', models.CharField(max_length=50)),
                ('brand', models.CharField(max_length=50)),
                ('vin', models.CharField(max_length=17)),
                ('motor', models.CharField(max_length=17)),
            ],
        ),
        migrations.CreateModel(
            name='Description',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_issue', models.DateTimeField(default=django.utils.timezone.now)),
                ('description', models.CharField(max_length=2500)),
                ('car', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='app.car')),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('document_number', models.PositiveIntegerField(blank=True)),
                ('phone_number', models.PositiveIntegerField(blank=True)),
                ('admin', models.BooleanField(default=False)),
                ('address', models.CharField(max_length=50)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='car',
            name='client',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='app.client'),
        ),
    ]
