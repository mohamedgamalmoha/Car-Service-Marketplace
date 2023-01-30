# Generated by Django 3.2 on 2023-01-27 13:55

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workshop', '0012_auto_20230126_2308'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='description_ar',
            field=models.CharField(max_length=500, null=True, verbose_name='Description'),
        ),
        migrations.AddField(
            model_name='service',
            name='description_en',
            field=models.CharField(max_length=500, null=True, verbose_name='Description'),
        ),
        migrations.AddField(
            model_name='service',
            name='name_ar',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Name'),
        ),
        migrations.AddField(
            model_name='service',
            name='name_en',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Name'),
        ),
        migrations.AddField(
            model_name='service',
            name='service_type_ar',
            field=models.CharField(choices=[('1', 'Related To Brand'), ('0', 'Not Related To Brand')], max_length=50, null=True, verbose_name='Service Type'),
        ),
        migrations.AddField(
            model_name='service',
            name='service_type_en',
            field=models.CharField(choices=[('1', 'Related To Brand'), ('0', 'Not Related To Brand')], max_length=50, null=True, verbose_name='Service Type'),
        ),
        migrations.AddField(
            model_name='workshop',
            name='description_ar',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Description'),
        ),
        migrations.AddField(
            model_name='workshop',
            name='description_en',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Description'),
        ),
        migrations.AddField(
            model_name='workshop',
            name='name_ar',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Name'),
        ),
        migrations.AddField(
            model_name='workshop',
            name='name_en',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Name'),
        ),
        migrations.AddField(
            model_name='workshoplocation',
            name='address_ar',
            field=models.CharField(max_length=400, null=True, verbose_name='Address'),
        ),
        migrations.AddField(
            model_name='workshoplocation',
            name='address_en',
            field=models.CharField(max_length=400, null=True, verbose_name='Address'),
        ),
        migrations.AddField(
            model_name='workshopvideo',
            name='title_ar',
            field=models.CharField(max_length=150, null=True, verbose_name='Title'),
        ),
        migrations.AddField(
            model_name='workshopvideo',
            name='title_en',
            field=models.CharField(max_length=150, null=True, verbose_name='Title'),
        ),
    ]
