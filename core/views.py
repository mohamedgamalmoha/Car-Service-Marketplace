from http import HTTPStatus

from django.shortcuts import render
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


def page_not_found_view(request, exception=None):
    context = {
        'status': HTTPStatus.NOT_FOUND.real,
        'message': 'Page Not Found'
    }
    return render(request, "errors/404.html", context, status=context.get('status', None))


def error_view(request, exception=None):
    context = {
        'status': HTTPStatus.INTERNAL_SERVER_ERROR.real,
        'message': 'An error happens in our backend, if it continues, please get in touch with us as soon as possible'
    }
    return render(request, "errors/500.html", context, status=context.get('status', None))


def permission_denied_view(request, exception=None):
    context = {
        'status': HTTPStatus.FORBIDDEN.real,
        'message': 'You are not authorized to view this page or do this action'
    }
    return render(request, "errors/403.html", context, status=context.get('status', None))


def bad_request_view(request, exception=None):
    context = {
        'status': HTTPStatus.BAD_REQUEST.real,
        'message': 'Our server cannot or will not process the request due to something that is perceived to be a client error'
    }
    return render(request, "errors/400.html", context, status=context.get('status', None))
