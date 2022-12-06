from django.db import models
from django.utils.safestring import mark_safe
from colorfield.fields import ColorField

from accounts.models import Customer


class Brand(models.Model):
    name = models.CharField("Name", max_length=40, null=True)
    image = models.ImageField("Logo", upload_to='customers/cars/', null=True)
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.name

    def show_image(self, width: int = 150, height: int = 100):
        url = self.image.url
        return mark_safe(f'<a href="{url}"> <img src="{url}" width="{width}" height={height} /></a>')


class Car(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, related_name='cars', null=True)
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, related_name='cars', null=True)
    model = models.CharField("Model", max_length=40, blank=True, null=True)
    number = models.CharField("Car Number", max_length=40, blank=True, null=True)
    model_year = models.DateField("Model Year", null=True)
    color = ColorField("Color", default='#000000', format="hexa")
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return str(self.model)
