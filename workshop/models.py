from django.db import models
from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator, MinValueValidator
from ckeditor.fields import RichTextField

from car.models import Brand
from accounts.models import Customer, PhoneNumberValidator


def validate_map_link(value: str):
    if not value.startswith('<iframe src="https://www.google.com/maps/') or not value.endswith('></iframe>'):
        raise ValidationError(
            _('%(value)s is not a valid map link'),
            params={'value': value},
        )


class ServiceType(models.TextChoices):
    BRAND = 1, "Related To Brand"
    NONE = 0, "Not Related To Brand"


class Service(models.Model):
    name = models.CharField("Name", max_length=150, blank=True, null=True)
    service_type = models.CharField("Service Type", max_length=50, choices=ServiceType.choices)
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.name


class WorkShopManager(models.Manager):

    def active(self):
        return self.filter(is_active=True)


class WorkShop(models.Model):
    name = models.CharField("Name", max_length=150, blank=True, null=True)
    description = RichTextField(null=True)
    phone_number = models.CharField("Phone Number", max_length=11, validators=[PhoneNumberValidator, ])
    whatsapp = models.CharField("Whatsapp number", max_length=11, validators=[PhoneNumberValidator, ])
    brands = models.ManyToManyField(Brand)
    services = models.ManyToManyField(Service)
    image = models.ImageField(upload_to='workshops/images/', blank=True, null=True)
    is_active = models.BooleanField("Activate", default=True)
    open_at = models.TimeField(null=True)
    close_at = models.TimeField(null=True)
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)

    objects = WorkShopManager()

    def __str__(self):
        return self.name

    def avg_rate(self):
        return self.rates.aggregate(models.Avg('value')).get('value__avg', None)

    def count_rate(self):
        return self.rates.count()

    def count_comment(self):
        return self.comments.count()

    def count_reports(self):
        return self.reports.count()

    def show_image(self, width: int = 150, height: int = 100):
        url = self.image.url
        return mark_safe(f'<a href="{url}"> <img src="{url}" width="{width}" height={height} /></a>')


class WorkShopLocation(models.Model):
    workshop = models.ForeignKey(WorkShop,  on_delete=models.CASCADE, null=True, related_name='locations')
    link = models.TextField(null=True, blank=True, validators=[validate_map_link])
    address = models.CharField(max_length=400)

    def show_map(self):
        return mark_safe(f"{self.link}")


class WorkShopVideo(models.Model):
    title = models.CharField(max_length=150)
    workshop = models.ForeignKey(WorkShop,  on_delete=models.CASCADE, null=True, related_name='videos')
    link = models.URLField()

    def show_link(self):
        return mark_safe(f"<a href='{self.link}'>{self.title}</a>")


class Rate(models.Model):
    customer = models.ForeignKey(Customer,  on_delete=models.SET_NULL, null=True)
    workshop = models.ForeignKey(WorkShop,  on_delete=models.SET_NULL, null=True, related_name='rates')
    value = models.IntegerField(null=True, blank=True, validators=[MinValueValidator(0), MaxValueValidator(5)])
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        verbose_name_plural = 'Rating'


class Comment(models.Model):
    customer = models.ForeignKey(Customer,  on_delete=models.SET_NULL, null=True)
    workshop = models.ForeignKey(WorkShop,  on_delete=models.SET_NULL, null=True, related_name='comments')
    title = models.CharField(max_length=350, null=True, blank=True)
    comment = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, null=False)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name_plural = 'Comment'


class ReportIssue(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    workshop = models.ForeignKey(WorkShop, on_delete=models.SET_NULL, null=True, related_name='reports')
    title = models.CharField(max_length=200)
    description = models.TextField()
    suggestion = models.TextField(null=True, blank=True)
    attachment = models.FileField(upload_to='reports/', null=True, blank=True,
                                  help_text="Upload any kind of attachment that could help to clarify more about the issue")
    date_of_issue = models.DateTimeField("When the issue occurred?", null=True)
    created = models.DateTimeField(auto_now_add=True, null=False)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
