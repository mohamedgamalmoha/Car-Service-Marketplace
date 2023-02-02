from django import template
from django.conf import settings


register = template.Library()


@register.filter(name='absolut_url')
def modify_url(value: str):
    languages = getattr(settings, 'LANGUAGES', None)
    if languages is None:
        return value
    for lang, _ in languages:
        value = value.replace(lang, '')
    if value.startswith('//'):
        value = value[1:]
    return value


@register.filter(name='is_current_url')
def check_current_url(value_1: str, value_2: str):
    url_1, url_2 = modify_url(value_1), modify_url(value_2)
    return url_1 == url_2
