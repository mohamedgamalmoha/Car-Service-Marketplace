from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView

from .models import Booking
from .forms import CreateBookingForm, UpdateBookingForm
from accounts.mixins import CustomerAuthMixIn


class CreateBookingView(CustomerAuthMixIn, CreateView):
    model = Booking
    form_class = CreateBookingForm
    template_name = 'booking/create.html'
    success_url = reverse_lazy('accounts:profile')
    extra_context = {
        'title': 'Book Service'
    }

    def form_valid(self, form):
        form.instance.customer = self.request.user
        return super().form_valid(form)


class UpdateBookingView(CustomerAuthMixIn, UpdateView):
    model = Booking
    form_class = UpdateBookingForm
    template_name = 'booking/update.html'
    success_url = reverse_lazy('accounts:profile')
    extra_context = {
        'title': 'Update Booking'
    }

    def get_queryset(self):
        return self.model.objects.filter(customer=self.request.user)
