# Generated by Django 3.2 on 2022-12-30 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0004_booking_commission_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='schedule_at',
            field=models.DateTimeField(help_text='When would you like to book?', verbose_name='Schedule Maintenance At'),
        ),
    ]
