# Generated by Django 3.2 on 2022-12-28 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0006_alter_brand_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='last_maintenance_date',
            field=models.DateField(help_text='When did the last maintenance happen?', null=True, verbose_name='Last Maintenance Date'),
        ),
        migrations.AddField(
            model_name='car',
            name='last_maintenance_details',
            field=models.TextField(help_text='Tell us more about what happened in the last maintenance', null=True, verbose_name='Last Maintenance Date'),
        ),
        migrations.AddField(
            model_name='car',
            name='last_oil_change_date',
            field=models.DateField(help_text='When did the last oil change happen?', null=True, verbose_name='Last Oil Change Date'),
        ),
        migrations.AddField(
            model_name='car',
            name='mileage',
            field=models.IntegerField(help_text='The number of miles or the average distance that a vehicle can travel on a specified quantity of fuel', null=True, verbose_name='Mileage'),
        ),
    ]
