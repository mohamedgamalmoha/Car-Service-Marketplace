# Generated by Django 3.2 on 2022-12-28 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0003_auto_20221228_2002'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='commission_status',
            field=models.CharField(choices=[('1', 'Collected'), ('0', 'Not Collected')], default='0', max_length=50, null=True, verbose_name='Commission Status'),
        ),
    ]
