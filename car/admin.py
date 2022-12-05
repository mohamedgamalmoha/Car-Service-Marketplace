from django.contrib import admin

from .models import Car, Brand


class BrandAdmin(admin.ModelAdmin):
    list_display = ['name', 'created', 'updated', 'show_image']
    readonly_fields = ['show_image']


class CarAdmin(admin.ModelAdmin):
    ...


admin.site.register(Car, CarAdmin)
admin.site.register(Brand, BrandAdmin)
