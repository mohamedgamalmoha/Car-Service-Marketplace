from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from .models import ContactUs, FAQs, AboutUs, TermsOfService, Works, CookiePolicy, PrivacyPolicy
from .forms import ContactUsForm


class ContactUsView(CreateView):
    model = ContactUs
    form_class = ContactUsForm
    success_url = reverse_lazy('home')
    template_name = "info/contact_us.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['title'] = self.model._meta.verbose_name
        return context


class BaseListView(ListView):
    context_object_name = 'objects'
    template_name = 'info/content.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['title'] = self.model._meta.verbose_name
        return context


class FAQsListView(BaseListView):
    model = FAQs


class AboutUsListView(BaseListView):
    model = AboutUs


class TermsOfServiceListView(BaseListView):
    model = TermsOfService


class WorksListView(BaseListView):
    model = Works


class CookiePolicyListView(BaseListView):
    model = CookiePolicy


class PrivacyPolicyListView(BaseListView):
    model = PrivacyPolicy
