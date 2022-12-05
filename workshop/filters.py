import django_filters
from django.db import models

from car.models import Brand
from .models import Service, WorkShop


class WorkShopOrderingFilter(django_filters.OrderingFilter):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.extra['choices'] += [
            ('rate', 'Rate'),
            ('-rate', 'Rate (descending)'),
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
    search = django_filters.CharFilter(method='search_filter', label='Search')
    brands = django_filters.ModelMultipleChoiceFilter(queryset=Brand.objects.all())
    services = django_filters.ModelMultipleChoiceFilter(queryset=Service.objects.all())
    ordering = WorkShopOrderingFilter()

    class Meta:
        model = WorkShop
        fields = ('search', 'brands', 'services', 'ordering')

    def search_filter(self, queryset, name, value):
        return queryset.filter(
            models.Q(title__icontains=value) | models.Q(description__icontains=value)
        )
