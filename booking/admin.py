from django.contrib import admin

from .models import Coupon, Discount, Booking


class CouponAdmin(admin.ModelAdmin):
    display_list = ('type', 'value', 'valid_from', 'valid_until', 'create_at', 'update_at')
    list_filter = ('type', )


class DiscountAdmin(admin.ModelAdmin):
    display_list = ('workshop', 'service', 'type', 'value', 'valid_from', 'valid_until', 'create_at', 'update_at')
    list_filter = ('type', )


class BookingAdmin(admin.ModelAdmin):
    display_list = ('customer', 'workshop', 'service', 'status', 'create_at', 'update_at')
    list_filter = ('status', 'commission_status', ('create_at', admin.DateFieldListFilter),)


admin.site.register(Coupon, CouponAdmin)
admin.site.register(Discount, DiscountAdmin)
admin.site.register(Booking, BookingAdmin)
