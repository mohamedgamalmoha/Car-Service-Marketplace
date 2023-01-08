from django.db import models
from colorfield.fields import ColorField
from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _

from accounts.models import Customer


class Brand(models.Model):
    name = models.CharField("Name", max_length=40, null=True)
    image = models.ImageField("Logo", upload_to='brands/', null=True)
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
    mileage = models.IntegerField(_("Mileage"), null=True, help_text=_("The number of miles or the average distance that a vehicle can travel on a specified quantity of fuel"))
    last_oil_change_date = models.DateField(_("Last Oil Change Date"), null=True, help_text=_("When did the last oil change happen?"))
    last_maintenance_date = models.DateField(_("Last Maintenance Date"), null=True, help_text=_("When did the last maintenance happen?"))
    last_maintenance_details = models.TextField(_("Last Maintenance Details"), null=True, help_text=_("Tell us more about what happened in the last maintenance"))
    color = models.CharField("Color", default='#000000', max_length=20)
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        verbose_name = 'Customer`s Car'
        verbose_name_plural = 'Customers` Cars'

    def __str__(self):
        return str(self.model)
