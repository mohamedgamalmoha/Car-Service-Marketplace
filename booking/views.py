from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.messages.views import SuccessMessageMixin

from car.models import Car
from .models import Booking, Discount
from accounts.mixins import CustomerAuthMixIn
from .forms import CreateBookingForm, UpdateBookingForm
from .utils import get_object_or_none


class CreateBookingView(CustomerAuthMixIn, SuccessMessageMixin, CreateView):
    model = Booking
    form_class = CreateBookingForm
    template_name = 'booking/create.html'
    success_url = reverse_lazy('accounts:profile')
    success_message = _("Your booking has successfully completed !!, "
                        "customer support will contact you soon, "
                        "for more info please checkout your profile")
    extra_context = {
        'title': _('Book A Service')
    }

    def get_initial(self):
        initial = super().get_initial()
        discount_session = get_object_or_none(Discount, pk=self.request.session.get('discount', None))
        if discount_session:
            initial.update({
                'workshop': discount_session.workshop.id,
                'service': discount_session.service.id,
                'discount': discount_session.id,
            })
        return initial

    def post(self, request, *args, **kwargs):
        discount = request.POST.get('discount', None)
        if discount:
            request.session.update({'discount': discount})
        return super().post(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(CreateBookingView, self).get_context_data(**kwargs)
        context['form'].fields['service'].widget.attrs['disabled'] = 'disabled'
        context['form'].fields['workshop'].widget.attrs['disabled'] = 'disabled'
        context['form'].fields['discount'].widget.attrs['disabled'] = 'disabled'
        context['form'].fields['car'].queryset = Car.objects.filter(customer=self.request.user)
        return context

    def form_valid(self, form):
        discount = get_object_or_none(Discount, pk=self.request.session.get('discount', None))
        if discount is not None:
            form.instance.discount = discount
            form.instance.service = discount.service
            form.instance.workshop = discount.workshop
        form.instance.customer = self.request.user
        return super().form_valid(form)


class UpdateBookingView(CustomerAuthMixIn, UpdateView):
    model = Booking
    form_class = UpdateBookingForm
    template_name = 'booking/update.html'
    success_url = reverse_lazy('accounts:profile')
    extra_context = {
        'title': _('Update Booking')
    }

    def get_queryset(self):
        return self.model.objects.filter(customer=self.request.user)
