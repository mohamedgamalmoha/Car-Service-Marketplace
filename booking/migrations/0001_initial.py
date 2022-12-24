# Generated by Django 3.2 on 2022-12-19 19:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('workshop', '0007_auto_20221213_1308'),
        ('accounts', '0003_auto_20221205_0009'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('0', 'FIXED'), ('1', 'PERCENTAGE'), ('2', 'FREE')], max_length=50, verbose_name='Coupon Type')),
                ('code', models.CharField(help_text='Leaving this field empty will generate a random code.', max_length=100, unique=True, verbose_name='Code')),
                ('value', models.DecimalField(decimal_places=3, max_digits=8, verbose_name='Value')),
                ('customer_limit', models.PositiveIntegerField(default=1, verbose_name='Customer Limit')),
                ('max_limit', models.PositiveIntegerField(default=10, verbose_name='Maximum Limit')),
                ('valid_from', models.DateField(blank=True, null=True, verbose_name='Valid From')),
                ('valid_until', models.DateField(help_text='Leaving this field empty will generate a random code.', verbose_name='Valid Till')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='Creation Date')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='Update Date')),
            ],
            options={
                'verbose_name': 'Coupon',
                'verbose_name_plural': 'Coupons',
                'ordering': ('create_at',),
            },
        ),
        migrations.CreateModel(
            name='Discount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('0', 'FIXED'), ('1', 'PERCENTAGE'), ('2', 'FREE')], max_length=50, verbose_name='Coupon Type')),
                ('value', models.DecimalField(decimal_places=3, max_digits=8, verbose_name='Value')),
                ('valid_from', models.DateField(verbose_name='Valid From')),
                ('valid_until', models.DateField(help_text='Leaving this field empty will generate a random code.', verbose_name='Valid Till')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='Creation Date')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='Update Date')),
                ('service', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='discounts', to='workshop.service', verbose_name='Service')),
                ('workshop', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='discounts', to='workshop.workshop', verbose_name='Workshop')),
            ],
            options={
                'verbose_name': 'Discount',
                'verbose_name_plural': 'Discount',
                'ordering': ('create_at',),
            },
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('0', 'PLACED'), ('1', 'ESTIMATED'), ('2', 'PAID'), ('3', 'CANCELED'), ('4', 'FAILED')], default='0', max_length=50, verbose_name='Booking Status')),
                ('estimated_price', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='Estimated Price')),
                ('note', models.TextField(blank=True, max_length=400, null=True, verbose_name='Note')),
                ('schedule_at', models.DateTimeField(verbose_name='Estimated Price')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='Creation Date')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='Update Date')),
                ('coupon', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='bookings', to='booking.coupon', verbose_name='Coupon')),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='bookings', to='accounts.customer', verbose_name='Customer')),
                ('discount', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='bookings', to='booking.discount', verbose_name='Discount')),
                ('service', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bookings', to='workshop.service', verbose_name='Service')),
                ('workshop', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bookings', to='workshop.workshop', verbose_name='Workshop')),
            ],
        ),
    ]