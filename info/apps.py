from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class InfoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'info'
    verbose_name = _('Info')
