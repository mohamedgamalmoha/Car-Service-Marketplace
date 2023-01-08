# Generated by Django 3.2 on 2023-01-08 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0007_auto_20221228_2002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='color',
            field=models.CharField(default='#000000', max_length=20, verbose_name='Color'),
        ),
        migrations.AlterField(
            model_name='car',
            name='last_maintenance_details',
            field=models.TextField(help_text='Tell us more about what happened in the last maintenance', null=True, verbose_name='Last Maintenance Details'),
        ),
    ]
