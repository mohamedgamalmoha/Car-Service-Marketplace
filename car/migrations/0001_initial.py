# Generated by Django 3.2 on 2022-12-04 21:39

import colorfield.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0002_auto_20221204_2019'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=40, null=True, verbose_name='Name')),
                ('image', models.ImageField(blank=True, null=True, upload_to='customers/cars/', verbose_name='Logo')),
            ],
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(blank=True, max_length=40, null=True, verbose_name='Model')),
                ('number', models.CharField(blank=True, max_length=40, null=True, verbose_name='Car Number')),
                ('model_year', models.DateField(null=True, verbose_name='Model Year')),
                ('color', colorfield.fields.ColorField(default='#000000', image_field=None, max_length=18, samples=None)),
                ('brand', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='cars', to='car.brand')),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='cars', to='accounts.customerprofile')),
            ],
        ),
    ]