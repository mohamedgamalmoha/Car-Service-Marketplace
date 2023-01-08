from django.views.generic import TemplateView

from car.models import Brand
from booking.models import Discount
from workshop.models import WorkShop
from info.models import MainInfo, HeaderImage


class HomePage(TemplateView):
    template_name = 'home.html'
    extra_context = {
        'brands': Brand.objects.all(),
        'workshops': WorkShop.objects.all(),
        'discounts': Discount.objects.all(),
        'main_info': MainInfo.objects.first(),
        'header_images': HeaderImage.objects.active(),
    }
