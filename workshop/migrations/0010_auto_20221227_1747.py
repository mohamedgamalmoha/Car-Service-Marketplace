# Generated by Django 3.2 on 2022-12-27 15:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20221205_0009'),
        ('workshop', '0009_service_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='comments', to='accounts.customer'),
        ),
        migrations.AlterField(
            model_name='rate',
            name='customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='rates', to='accounts.customer'),
        ),
        migrations.AlterField(
            model_name='reportissue',
            name='customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='reports', to='accounts.customer'),
        ),
    ]
