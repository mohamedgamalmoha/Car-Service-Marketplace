from django import forms
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError

from .utils import get_object_or_none
from accounts.forms import BaseUpdateCSSClassForm
from .models import Coupon, Booking, BookingStatus


class CreateBookingForm(BaseUpdateCSSClassForm, forms.ModelForm):
    coupon = forms.CharField(required=False)
    field_order = ('workshop', 'service', 'discount')

    def __init__(self, *args, **kwargs):
        super(CreateBookingForm, self).__init__(*args, **kwargs)
        for field_name in self.field_order:
            self.fields[field_name].required = False

    class Meta:
        model = Booking
        exclude = ('customer', 'status', 'estimated_price', 'earned_amount', 'commission_status', 'expense_amount',
                   'create_at', 'update_at')
        help_texts = {
            'coupon': _('If you have a coupon write it, otherwise leave it as it is')
        }
        widgets = {
            'schedule_at': forms.widgets.NumberInput(attrs={'type': 'date'})
        }

    def clean_coupon(self):
        code = self.cleaned_data.get('coupon', None)
        if code is None or len(code) == 0:
            return None
        obj = get_object_or_none(Coupon, code=code)
        if obj is None:
            raise ValidationError(_("Invalid Code"))
        return obj

    def clean_schedule_at(self):
        schedule_at = self.cleaned_data.get('schedule_at', None)
        if schedule_at < timezone.now():
            raise ValidationError(_("Date should be in the future"))
        return schedule_at


class UpdateBookingForm(BaseUpdateCSSClassForm, forms.ModelForm):
    status = forms.ChoiceField(choices=BookingStatus.customer_choices())

    class Meta:
        model = Booking
        fields = ('status', 'note')
