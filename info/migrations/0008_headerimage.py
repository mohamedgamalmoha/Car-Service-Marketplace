# Generated by Django 3.2 on 2022-12-28 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0007_maininfo_why_us'),
    ]

    operations = [
        migrations.CreateModel(
            name='HeaderImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alt', models.CharField(max_length=250)),
                ('image', models.ImageField(upload_to='home/header')),
                ('active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Home Page Image',
                'verbose_name_plural': 'Home Page Images',
            },
        ),
    ]
