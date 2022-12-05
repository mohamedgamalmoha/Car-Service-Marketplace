# Generated by Django 3.2 on 2022-12-05 14:28

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20221205_0009'),
        ('workshop', '0002_auto_20221205_1613'),
    ]

    operations = [
        migrations.RenameField(
            model_name='workshop',
            old_name='brand',
            new_name='brands',
        ),
        migrations.CreateModel(
            name='ReportIssue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('suggestion', models.TextField(blank=True, null=True)),
                ('attachment', models.FileField(blank=True, null=True, upload_to='reports/')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.customer')),
                ('workshop', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='workshop.workshop')),
            ],
        ),
        migrations.CreateModel(
            name='Rate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)])),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.customer')),
                ('workshop', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='workshop.workshop')),
            ],
            options={
                'verbose_name_plural': 'Rating',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=350, null=True)),
                ('comment', models.TextField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.customer')),
                ('workshop', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='workshop.workshop')),
            ],
            options={
                'verbose_name_plural': 'Comment',
            },
        ),
    ]
