# Generated by Django 3.2 on 2023-01-27 20:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workshop', '0013_auto_20230127_1555'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='service_type_ar',
        ),
        migrations.RemoveField(
            model_name='service',
            name='service_type_en',
        ),
    ]
