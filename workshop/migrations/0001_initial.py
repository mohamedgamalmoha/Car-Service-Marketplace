# Generated by Django 3.2 on 2022-12-05 14:12

import django.core.validators
from django.db import migrations, models
import workshop.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('car', '0003_auto_20221205_0215'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=150, null=True, verbose_name='Name')),
                ('service_type', models.CharField(choices=[('0', 'Not Related To Brand'), ('1', 'Related To Brand')], max_length=50, verbose_name='Service Type')),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='WorkShop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=150, null=True, verbose_name='Name')),
                ('phone_number', models.CharField(max_length=11, validators=[django.core.validators.RegexValidator('^[0-9]{11}$', 'Invalid Phone Number')], verbose_name='Phone Number')),
                ('whatsapp', models.CharField(max_length=11, validators=[django.core.validators.RegexValidator('^[0-9]{11}$', 'Invalid Phone Number')], verbose_name='Whatsapp number')),
                ('map_link', models.TextField(blank=True, null=True, validators=[workshop.models.validate_map_link])),
                ('image', models.ImageField(blank=True, null=True, upload_to='workshops/images/')),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('brand', models.ManyToManyField(null=True, to='car.Brand')),
                ('services', models.ManyToManyField(null=True, to='workshop.Service')),
            ],
        ),
    ]
