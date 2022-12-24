from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from .utils import get_object_or_none
from .models import Coupon, Booking, BookingStatus


class CreateBookingForm(forms.ModelForm):
    coupon = forms.CharField()

    class Meta:
        model = Booking
        exclude = ('estimated_price', 'create_at', 'update_at')

    def clean_coupon(self):
        code = self.cleaned_data['coupon']
        if code is None:
            return None
        obj = get_object_or_none(Coupon, code=code)
        if obj is None:
            raise ValidationError(_("Invalid Code"))
        return obj


class UpdateBookingForm(forms.ModelForm):
    status = forms.ChoiceField(choices=BookingStatus.customer_choices())

    class Meta:
        model = Booking
        fields = ('status', 'note')
