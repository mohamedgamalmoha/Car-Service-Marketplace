# Generated by Django 3.2 on 2022-12-08 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0002_contactus'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactus',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='contactus',
            name='updated',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
