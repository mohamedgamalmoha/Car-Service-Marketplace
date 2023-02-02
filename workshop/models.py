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
    BRAND = 1, _("Related To Brand")
    NONE = 0, _("Not Related To Brand")


class Service(models.Model):
    name = models.CharField(verbose_name=_("Name"), max_length=150, blank=True, null=True)
    description = models.CharField(verbose_name=_("Description"), null=True, max_length=500)
    service_type = models.CharField(verbose_name=_("Service Type"), max_length=50, choices=ServiceType.choices)
    created = models.DateTimeField(verbose_name=_("Created"), auto_now_add=True, null=True)
    updated = models.DateTimeField(verbose_name=_("Updated"), auto_now=True, null=True)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = _('Service')
        verbose_name_plural = _('Services')


class WorkShopManager(models.Manager):

    def active(self):
        return self.filter(is_active=True)


class WorkShop(models.Model):
    name = models.CharField(verbose_name=_("Name"), max_length=150, blank=True, null=True)
    description = RichTextField(verbose_name=_("Description"), null=True)
    phone_number = models.CharField(verbose_name=_("Phone Number"), max_length=11, validators=[PhoneNumberValidator, ])
    whatsapp = models.CharField(verbose_name=_("Whatsapp number"), max_length=11, validators=[PhoneNumberValidator, ])
    brands = models.ManyToManyField(Brand, verbose_name=_("Brands"))
    services = models.ManyToManyField(Service, verbose_name=_("Services"))
    image = models.ImageField(verbose_name=_("Image"), upload_to='workshops/images/', blank=True, null=True)
    is_active = models.BooleanField(verbose_name=_("Activate"), default=True)
    open_at = models.TimeField(verbose_name=_("Open At"), null=True)
    close_at = models.TimeField(verbose_name=_("Close At"), null=True)
    model_year_start = models.DateField(verbose_name=_("Model Year Start"), null=True)
    model_year_end = models.DateField(verbose_name=_("Model Year End"), null=True)
    created = models.DateTimeField(verbose_name=_("Created"), auto_now_add=True, null=True)
    updated = models.DateTimeField(verbose_name=_("Updated"), auto_now=True, null=True)

    objects = WorkShopManager()

    class Meta:
        verbose_name = _('WorkShop')
        verbose_name_plural = _('WorkShops')

    def __str__(self):
        return str(self.name)

    def avg_rate(self):
        return self.rates.aggregate(models.Avg('value')).get('value__avg', None)
    avg_rate.short_description = _("Average Rate")

    def count_rate(self):
        return self.rates.count()
    count_rate.short_description = _("Count Rate")

    def count_comment(self):
        return self.comments.count()
    count_comment.short_description = _("Count Comment")

    def count_reports(self):
        return self.reports.count()
    count_reports.short_description = _("Count Report")

    def show_image(self, width: int = 150, height: int = 100):
        url = self.image.url
        return mark_safe(f'<a href="{url}"> <img src="{url}" width="{width}" height={height} /></a>')
    show_image.short_description = _("Show Image")

    @property
    def video(self):
        return self.videos.first()

    def rate_starts(self):
        rate = int(self.avg_rate() or 0)
        if rate == 0:
            return ('fa-regular' for _ in range(5))
        starts = ['fa-solid' for _ in range(rate)]
        starts.extend(['fa-regular' for _ in range(5-rate)])
        return tuple(starts)


class WorkShopLocation(models.Model):
    workshop = models.ForeignKey(WorkShop,  on_delete=models.CASCADE, null=True, related_name='locations', verbose_name=_("Workshop"))
    link = models.TextField(verbose_name=_("Link"), null=True, blank=True, validators=[validate_map_link])
    address = models.CharField(verbose_name=_("Address"), max_length=400)

    class Meta:
        verbose_name = _('WorkShop Location')
        verbose_name_plural = _('WorkShop Locations')

    def show_map(self):
        return mark_safe(f"{self.link}")
    show_map.short_description = _("Show Map")


class WorkShopVideo(models.Model):
    title = models.CharField(verbose_name=_("Title"), max_length=150)
    workshop = models.ForeignKey(WorkShop,  on_delete=models.CASCADE, null=True, related_name='videos', verbose_name=_("Workshop"))
    link = models.URLField(verbose_name=_("Link"))

    class Meta:
        verbose_name = _('Work Shop Video')
        verbose_name_plural = _('Work Shop Videos')

    def show_link(self):
        return mark_safe(f"<a href='{self.link}'>{self.title}</a>")
    show_link.short_description = _("Show Link")


class Rate(models.Model):
    customer = models.ForeignKey(Customer,  on_delete=models.SET_NULL, null=True, related_name='rates', verbose_name=_("Customer"))
    workshop = models.ForeignKey(WorkShop,  on_delete=models.SET_NULL, null=True, related_name='rates', verbose_name=_("Workshop"))
    value = models.IntegerField(null=True, blank=True, validators=[MinValueValidator(0), MaxValueValidator(5)], verbose_name=_("Value"))
    created = models.DateTimeField(auto_now_add=True, null=True, verbose_name=_("Created"))
    updated = models.DateTimeField(auto_now=True, null=True, verbose_name=_("Updated"))

    class Meta:
        verbose_name = _('Rating')
        verbose_name_plural = _('Ratings')
        unique_together = ('customer', 'workshop')


class Comment(models.Model):
    customer = models.ForeignKey(Customer,  on_delete=models.SET_NULL, null=True, related_name='comments', verbose_name=_("Customer"))
    workshop = models.ForeignKey(WorkShop,  on_delete=models.SET_NULL, null=True, related_name='comments', verbose_name=_("Workshop"))
    title = models.CharField(max_length=350, null=True, blank=True, verbose_name=_("Title"))
    comment = models.TextField(null=True, blank=True, verbose_name=_("Comment"))
    created = models.DateTimeField(auto_now_add=True, null=False, verbose_name=_("Created"))
    updated = models.DateTimeField(auto_now=True, verbose_name=_("Updated"))

    def __str__(self):
        return self.customer.username

    class Meta:
        verbose_name = _('Comment')
        verbose_name_plural = _('Comments')


class ReportIssue(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, related_name='reports', verbose_name=_("Customer"))
    workshop = models.ForeignKey(WorkShop, on_delete=models.SET_NULL, null=True, related_name='reports', verbose_name=_('Workshop'))
    title = models.CharField(max_length=200, verbose_name=_("Title"))
    description = models.TextField(verbose_name=_("Description"))
    suggestion = models.TextField(null=True, blank=True, verbose_name=_("Suggestion"))
    attachment = models.FileField(upload_to='reports/', null=True, blank=True,
                                  help_text=_("Upload any kind of attachment that could help to clarify more about the issue"),
                                  verbose_name=_("Attachment"))
    date_of_issue = models.DateTimeField(null=True, verbose_name=_("When the issue occurred?"))
    created = models.DateTimeField(auto_now_add=True, null=False, verbose_name=_("Created"))
    updated = models.DateTimeField(auto_now=True, verbose_name=_("Updated"))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Report Issue')
        verbose_name_plural = _('Report Issues')
