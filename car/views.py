from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView

from .models import Car
from .forms import CarForm
from accounts.mixins import CustomerAuthMixIn


class CreateCarView(CustomerAuthMixIn, CreateView):
    model = Car
    form_class = CarForm
    template_name = "car/create.html"
    success_url = reverse_lazy('accounts:profile')
    extra_context = {
        'title': 'Add Car'
    }

    def form_valid(self, form):
        form.instance.customer = self.request.user
        return super().form_valid(form)


class UpdateCarView(CustomerAuthMixIn, UpdateView):
    model = Car
    form_class = CarForm
    template_name = "car/update.html"
    success_url = reverse_lazy('accounts:profile')
    extra_context = {
        'title': 'Update Car'
    }

    def get_queryset(self):
        return self.model.objects.filter(customer=self.request.user)
