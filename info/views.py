from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from .models import ContactUs, FAQs, AboutUs, TermsOfService, Works, CookiePolicy, PrivacyPolicy
from .forms import ContactUsForm


class ContactUsView(CreateView):
    model = ContactUs
    form_class = ContactUsForm
    success_url = reverse_lazy('home')
    template_name = "info/contact_us.html"
    extra_context = {'title': 'Contact Us'}


class BaseListView(ListView):
    context_object_name = 'objects'
    template_name = 'info/content.html'


class FAQsListView(BaseListView):
    model = FAQs
    extra_context = {
        'title': 'FAQs'
    }


class AboutUsListView(BaseListView):
    model = AboutUs
    extra_context = {
        'title': 'About Us'
    }


class TermsOfServiceListView(BaseListView):
    model = TermsOfService
    extra_context = {
        'title': 'Terms Of Service'
    }


class WorksListView(BaseListView):
    model = Works
    extra_context = {
        'title': 'How it works'
    }


class CookiePolicyListView(BaseListView):
    model = CookiePolicy
    extra_context = {
        'title': 'Cookie Policy'
    }


class PrivacyPolicyListView(BaseListView):
    model = PrivacyPolicy
    extra_context = {
        'title': 'Privacy Policy'
    }
