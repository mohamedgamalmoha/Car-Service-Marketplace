from django.contrib import admin
from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _

from .models import Coupon, Discount, Booking, Expense


class CouponAdmin(admin.ModelAdmin):
    display_list = ('type', 'value', 'valid_from', 'valid_until', 'create_at', 'update_at')
    list_filter = ('type', )


class DiscountAdmin(admin.ModelAdmin):
    display_list = ('workshop', 'service', 'type', 'value', 'valid_from', 'valid_until', 'create_at', 'update_at')
    list_filter = ('type', )


class BookingAdmin(admin.ModelAdmin):
    display_list = ('customer', 'workshop', 'service', 'status', 'create_at', 'update_at')
    list_filter = ('status', 'commission_status', ('create_at', admin.DateFieldListFilter),)
    readonly_fields = ('customer_phone_number', 'show_customer_whatsapp_link')

    def show_customer_whatsapp_link(self, obj):
        return mark_safe(f"<a href=\"{obj.customer_whatsapp_link}\" target=\"_blank\" style=\"text-decoration: none;\"><img src=\"/static/images/whatsapp.png\" style=\"width:50px; height:50px; border-radius:50%;\"></a>")
    show_customer_whatsapp_link.short_description = _("Whatsapp Link")


class ExpenseAdmin(admin.ModelAdmin):
    display_list = ('cause', 'amount', 'paid_at', 'create_at', 'update_at')
    list_filter = ('paid_at', )


admin.site.register(Coupon, CouponAdmin)
admin.site.register(Discount, DiscountAdmin)
admin.site.register(Booking, BookingAdmin)
admin.site.register(Expense, ExpenseAdmin)
