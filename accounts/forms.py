from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import Customer, CustomerProfile


class RegistrationForm(UserCreationForm):

    class Meta:
        model = Customer
        fields = ("username", "email", "first_name", "last_name", "password1", "password2")

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.fields.get('email').required = True

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


class CustomerProfileForm(forms.ModelForm):

    class Meta:
        model = CustomerProfile
        exclude = ('user', )
