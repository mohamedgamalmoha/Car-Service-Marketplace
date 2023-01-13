from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.messages.views import SuccessMessageMixin

from car.models import Car
from accounts.mixins import CustomerAuthMixIn
from workshop.models import WorkShop, Service
from .utils import get_object_or_none
from .models import Booking, Discount
from .forms import CreateBookingForm, UpdateBookingForm


class BaseCreatBookingView(CustomerAuthMixIn, SuccessMessageMixin, CreateView):
    model = Booking
    form_class = CreateBookingForm
    template_name = 'booking/create.html'
    success_url = reverse_lazy('accounts:profile')
    success_message = _("Your booking has successfully completed !!, "
                        "customer support will contact you soon, "
                        "for more updates please checkout your profile")
    extra_context = {
        'title': _('Book A Service')
    }

    def form_valid(self, form):
        form.instance.customer = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(BaseCreatBookingView, self).get_context_data(**kwargs)
        context['form'].fields['car'].queryset = Car.objects.filter(customer=self.request.user)
        return context


class CreateBookingWithDiscountView(BaseCreatBookingView):

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

    def form_valid(self, form):
        discount = get_object_or_none(Discount, pk=self.request.session.get('discount', None))
        if discount is not None:
            form.instance.discount = discount
            form.instance.service = discount.service
            form.instance.workshop = discount.workshop
        return super().form_valid(form)


class CreateBookingWithoutDiscountView(BaseCreatBookingView):

    def post(self, request, *args, **kwargs):
        discount = request.POST.get('workshop', None)
        if discount:
            request.session.update({'workshop': discount})
        return super().post(request, *args, **kwargs)

    def get_initial(self):
        initial = super().get_initial()
        workshop_session = get_object_or_none(WorkShop, pk=self.request.session.get('workshop', None))
        if workshop_session:
            initial.update({
                'workshop': workshop_session.id,
            })
        return initial

    def get_context_data(self, **kwargs):
        context = super(BaseCreatBookingView, self).get_context_data(**kwargs)
        workshop = self.get_initial().get('workshop', None)
        if workshop:
            context['form'].fields['service'].queryset = Service.objects.filter(workshop=workshop)
            context['form'].fields['service'].widget.attrs['disabled'] = False
            context['form'].fields['service'].widget.attrs["required"] = "required"
        context['form'].fields['discount'].widget.attrs['type'] = 'hidden'
        return context

    def form_valid(self, form):
        workshop = get_object_or_none(WorkShop, pk=self.request.session.get('workshop', None))
        if workshop is not None:
            form.instance.workshop = workshop
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
