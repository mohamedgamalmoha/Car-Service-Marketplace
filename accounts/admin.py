from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User, UserRole, CustomerProfile


class CustomerProfileInlineAdmin(admin.TabularInline):
    model = CustomerProfile
    extra = 0


class CustomerProfileAdmin(admin.ModelAdmin):
    list_display = ["name", "age", "gender"]
    list_filter = ["gender", ]
    list_per_page = 20


class CustomUserAdmin(UserAdmin):
    inlines = [
        CustomerProfileInlineAdmin
    ]

    def get_inlines(self, request, obj):
        return self.inlines if obj.role == UserRole.CUSTOMER else ()


admin.site.register(User, CustomUserAdmin)
admin.site.register(CustomerProfile, CustomerProfileAdmin)
