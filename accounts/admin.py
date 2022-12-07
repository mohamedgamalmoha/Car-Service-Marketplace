from django.db import models
from django.utils.timezone import localdate
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _


from .models import User, UserRole, CustomerProfile


class AgeCustomerListFilter(admin.SimpleListFilter):
    title = _('Age')
    parameter_name = 'age'

    def lookups(self, request, model_admin):
        return (
            ('18,30', _('in the twenties')),
            ('30,40', _('in the thirties')),
            ('40,50', _('in the forties ')),
            ('50,60', _('in the fifties ')),
            ('60,70', _('in the sixties ')),
            ('70,80', _('in the seventies')),
        )

    def queryset(self, request, queryset):
        val = self.value()
        if val is None:
            return queryset
        start_age, end_age = self.value().split(',')
        current_year = localdate().today().year
        start_year, end_year = current_year - int(end_age), current_year - int(start_age)
        return queryset.filter(
            models.Q(date_of_birth__year__gte=start_year) & models.Q(date_of_birth__year__lte=end_year)
        )


class CustomerProfileInlineAdmin(admin.TabularInline):
    model = CustomerProfile
    extra = 0
    min_num = 0
    max_num = 0
    can_delete = False
    fields = ('name', 'phone_number', 'city', 'state', 'address', 'gender', 'age')
    readonly_fields = ('name', 'phone_number', 'city', 'state', 'address', 'gender', 'age')


class CustomerProfileAdmin(admin.ModelAdmin):
    list_display = ["name", "age", "gender", "phone_number"]
    list_filter = ['gender', AgeCustomerListFilter]
    search_fields = ('user__first_name', 'user__last_name')
    list_per_page = 20


class CustomUserAdmin(UserAdmin):
    inlines = [
        CustomerProfileInlineAdmin
    ]

    def get_inlines(self, request, obj):
        return self.inlines if obj.role == UserRole.CUSTOMER else ()


admin.site.register(User, CustomUserAdmin)
admin.site.register(CustomerProfile, CustomerProfileAdmin)
