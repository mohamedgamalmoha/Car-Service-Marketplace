from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.views.generic import CreateView, UpdateView, DetailView, FormView
from django.contrib.auth.backends import get_user_model
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import login, update_session_auth_hash
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.contrib.messages.views import SuccessMessageMixin

from .mixins import CustomerAuthMixIn
from .models import UserRole, CustomerProfile
from .forms import RegistrationForm, CustomerProfileForm


User = get_user_model()
URL_REDIRECT = '/'


class LogInView(SuccessMessageMixin, LoginView):
    template_name = 'accounts/login.html'
    success_url = reverse_lazy('accounts:profile')
    redirect_authenticated_user = True
    success_message = 'Logged in successfully'
    extra_context = {
        'title': 'LogIn'
    }

    def get_success_url(self):
        if self.request.user.role == UserRole.CUSTOMER:
            return self.success_url
        return reverse_lazy('admin:index')


class RegistrationView(SuccessMessageMixin, CreateView):
    form_class = RegistrationForm
    template_name = 'accounts/register.html'
    success_message = 'Registration has been completed successfully'
    success_url = reverse_lazy('accounts:profile')
    extra_context = {
        'title': 'Registration'
    }

    def form_valid(self, form):
        user = form.save(commit=False)
        user.role = UserRole.CUSTOMER
        user.save()
        login(self.request, user)
        return HttpResponseRedirect(self.success_url)


class LogOutView(SuccessMessageMixin, LogoutView):
    template_name = 'accounts/logout.html'
    success_message = 'Logged out successfully'
    success_url = reverse_lazy(URL_REDIRECT)


class CustomerProfileView(CustomerAuthMixIn, DetailView):
    model = CustomerProfile
    template_name = 'accounts/profile.html'
    context_object_name = 'customer'
    extra_context = {
        'title': 'Profile'
    }

    def get_object(self):
        return self.request.user.profile


class UpdateCustomerProfileView(SuccessMessageMixin, CustomerAuthMixIn, UpdateView):
    model = CustomerProfile
    form_class = CustomerProfileForm
    success_url = reverse_lazy('accounts:profile')
    success_message = 'Your info has been updated successfully'
    template_name = 'accounts/profile_update.html'
    extra_context = {
        'title': 'Update Profile'
    }

    def get_object(self):
        return get_object_or_404(self.model, user=self.request.user)


class UserChangePasswordView(SuccessMessageMixin, PasswordChangeView):
    form_class = PasswordChangeForm
    template_name = 'accounts/user_change_password.html'
    success_message = 'Password has been updated successfully'
    extra_context = {'title': 'Change password'}
    success_url = reverse_lazy('home')
