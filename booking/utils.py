from django.db.models import Model
from django.core.exceptions import ObjectDoesNotExist


def get_object_or_none(model: Model, **kwargs):
    """Get object if existed, otherwise return none"""
    try:
        return model.objects.get(**kwargs)
    except ObjectDoesNotExist:
        return None
