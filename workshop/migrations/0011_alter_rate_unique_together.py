# Generated by Django 3.2 on 2023-01-07 11:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20221205_0009'),
        ('workshop', '0010_auto_20221227_1747'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='rate',
            unique_together={('customer', 'workshop')},
        ),
    ]