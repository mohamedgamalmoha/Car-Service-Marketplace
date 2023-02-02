from django import forms
from django.db import models
from django.utils.translation import gettext_lazy as _

import django_filters

from car.models import Brand
from .models import Service, WorkShop


class WorkShopOrderingFilter(django_filters.OrderingFilter):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.extra['choices'] += [
            ('rate', _('Rate')),
            ('-rate', _('Rate (descending)')),
        ]

    def filter(self, queryset, value):
        if value is None:
            return queryset
        if 'rate' in value:
            queryset = queryset.annotate(rate=models.Avg('rates__value')).order_by('rate')
        elif '-rate' in value:
            queryset = queryset.annotate(rate=models.Avg('rates__value')).order_by('-rate')
        return super().filter(queryset, value)


class WorkShopFilter(django_filters.FilterSet):
    search = django_filters.CharFilter(method='search_filter', label=_('Search'))
    brands = django_filters.ModelMultipleChoiceFilter(queryset=Brand.objects.all(), widget=forms.CheckboxSelectMultiple)
    services = django_filters.ModelMultipleChoiceFilter(queryset=Service.objects.all(), widget=forms.CheckboxSelectMultiple)
    ordering = WorkShopOrderingFilter()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Customize Search Field
        self.form.fields['search'].widget.attrs['class'] = 'bg-transparent px-4 py-1 text-white w-100'
        self.form.fields['search'].widget.attrs['placeholder'] = _("Search")
        self.form.fields['search'].widget.attrs['style'] = "border:none;border-bottom: 1px solid #F40612;"
        # Customize Ordering Field
        self.form.fields['ordering'].widget.attrs['class'] = 'form-control'
        self.form.fields['ordering'].widget.attrs['style'] = "border: 1px solid #f4061241; border-radius: 10px;" \
                                                             " background-color:#222222; color:white;"

    class Meta:
        model = WorkShop
        fields = ('search', 'brands', 'services', 'ordering')

    def search_filter(self, queryset, name, value):
        return queryset.filter(
            models.Q(name_en__icontains=value) | models.Q(name_ar__icontains=value) |
            models.Q(description_en__icontains=value) | models.Q(description_ar__icontains=value)
        )
