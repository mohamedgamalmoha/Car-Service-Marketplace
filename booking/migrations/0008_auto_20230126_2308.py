# Generated by Django 3.2 on 2023-01-26 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0007_expense'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='booking',
            options={'verbose_name': 'Booking', 'verbose_name_plural': 'Bookings'},
        ),
        migrations.AlterModelOptions(
            name='expense',
            options={'verbose_name': 'Expense', 'verbose_name_plural': 'Expenses'},
        ),
        migrations.AlterField(
            model_name='booking',
            name='create_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Creation'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='update_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Update'),
        ),
        migrations.AlterField(
            model_name='coupon',
            name='create_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Creation'),
        ),
        migrations.AlterField(
            model_name='coupon',
            name='update_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Update'),
        ),
        migrations.AlterField(
            model_name='discount',
            name='create_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Creation'),
        ),
        migrations.AlterField(
            model_name='discount',
            name='update_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Update'),
        ),
        migrations.AlterField(
            model_name='expense',
            name='create_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Creation'),
        ),
        migrations.AlterField(
            model_name='expense',
            name='update_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Update'),
        ),
    ]
