from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from modeltranslation.admin import TranslationAdmin

from .models import Car, Brand


class CarModalYearListFilter(admin.SimpleListFilter):
    title = _('Model Year')
    parameter_name = 'model_year'

    def lookups(self, request, model_admin):
        return((i, i) for i in Car.objects.values_list('model_year__year', flat=True))

    def queryset(self, request, queryset):
        if self.value() is None:
            return queryset
        return queryset.filter(model_year__year=self.value())


class BrandAdmin(TranslationAdmin):
    list_display = ['name', 'created', 'updated', 'show_image']
    readonly_fields = ['show_image']
    search_fields = ('name', )


class CarAdmin(admin.ModelAdmin):
    list_display = ['model', 'brand', 'customer', 'model_year', 'created', 'updated']
    list_filter = ['brand', CarModalYearListFilter]
    search_fields = ['model', 'brand__name']


admin.site.register(Car, CarAdmin)
admin.site.register(Brand, BrandAdmin)
