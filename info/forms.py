from django import forms

from .models import ContactUs
from accounts.forms import BaseUpdateCSSClassForm


class ContactUsForm(BaseUpdateCSSClassForm, forms.ModelForm):

    class Meta:
        model = ContactUs
        exclude = ('created', 'updated')
