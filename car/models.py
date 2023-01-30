from django.db import models
from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _

from accounts.models import Customer


class Brand(models.Model):
    name = models.CharField(max_length=40, null=True, verbose_name=_("Name"))
    image = models.ImageField(upload_to='brands/', null=True, verbose_name=_("Logo"))
    created = models.DateTimeField(auto_now_add=True, null=True, verbose_name=_("Created"))
    updated = models.DateTimeField(auto_now=True, null=True, verbose_name=_("Updated"))

    class Meta:
        verbose_name = _('Brand')
        verbose_name_plural = _('Brands')

    def __str__(self):
        return str(self.name)

    def show_image(self, width: int = 150, height: int = 100):
        url = self.image.url
        return mark_safe(f'<a href="{url}"> <img src="{url}" width="{width}" height={height} /></a>')
    show_image.short_description = _("Show Image")


class Car(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, related_name='cars', null=True, verbose_name=_("Customer"))
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, related_name='cars', null=True, verbose_name=_("Brand"))
    model = models.CharField(max_length=40, blank=True, null=True, verbose_name=_("Model"))
    number = models.CharField(max_length=40, blank=True, null=True, verbose_name=_("Number"))
    model_year = models.DateField(null=True, verbose_name=_("Model Year"))
    mileage = models.IntegerField(null=True,
                                  help_text=_("The number of miles or the average distance that a vehicle can travel on "
                                              "a specified quantity of fuel"),
                                  verbose_name=_("Mileage"))
    last_oil_change_date = models.DateField(null=True, help_text=_("When did the last oil change happen?"),
                                            verbose_name=_("Last Oil Change Date"))
    last_maintenance_date = models.DateField(null=True, help_text=_("When did the last maintenance happen?"),
                                             verbose_name=_("Last Maintenance Date"))
    last_maintenance_details = models.TextField(null=True, help_text=_("Tell us more about what happened in the last maintenance"),
                                                verbose_name=_("Last Maintenance Details"))
    color = models.CharField(default='#000000', max_length=20, verbose_name=_("Color"))
    created = models.DateTimeField(auto_now_add=True, null=True, verbose_name=_("Created"))
    updated = models.DateTimeField(auto_now=True, null=True, verbose_name=_("Updated"))

    class Meta:
        verbose_name = _('Customer`s Car')
        verbose_name_plural = _('Customers` Cars')

    def __str__(self):
        return str(self.model)
