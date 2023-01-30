from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class BookingConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'booking'
    verbose_name = _('Booking')
