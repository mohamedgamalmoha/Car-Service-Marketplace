from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class CarConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'car'
    verbose_name = _('Car')
