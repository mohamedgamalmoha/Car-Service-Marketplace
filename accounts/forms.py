from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm

from .models import Customer, CustomerProfile


class BaseUpdateCSSClassForm:
    css_class: str = 'form-control'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Customize Fields - css class -
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'


class LogInForm(BaseUpdateCSSClassForm, AuthenticationForm):
    ...


class RegistrationForm(BaseUpdateCSSClassForm, UserCreationForm):

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


class CustomerProfileForm(BaseUpdateCSSClassForm, forms.ModelForm):

    class Meta:
        model = CustomerProfile
        exclude = ('user', )


class UserChangePasswordForm(BaseUpdateCSSClassForm, PasswordChangeForm):
    ...
