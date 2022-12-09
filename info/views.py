from django.urls import reverse_lazy
from django.views.generic import CreateView

from .models import ContactUs
from .forms import ContactUsForm


class ContactUsView(CreateView):
    model = ContactUs
    form_class = ContactUsForm
    success_url = reverse_lazy('home')
    template_name = "info/contact_us.html"
    extra_context = {'title': 'Contact Us'}
