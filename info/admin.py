from django.contrib import admin

from .models import MainInfo, Works, AboutUs, TermsOfService, CookiePolicy, PrivacyPolicy, FAQs


class ModelAdmin(admin.ModelAdmin):

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        if self.model.objects.count() >= 1:
            return False
        return super().has_add_permission(request)


admin.site.register(FAQs)
admin.site.register(Works)
admin.site.register(AboutUs)
admin.site.register(CookiePolicy)
admin.site.register(PrivacyPolicy)
admin.site.register(TermsOfService)
admin.site.register(MainInfo, ModelAdmin)
