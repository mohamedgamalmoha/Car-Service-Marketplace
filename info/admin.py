from django.contrib import admin

from modeltranslation.admin import TranslationAdmin

from .models import MainInfo, Works, AboutUs, TermsOfService, CookiePolicy, PrivacyPolicy, FAQs, ContactUs, HeaderImage


class MainInfoAdmin(TranslationAdmin):
    readonly_fields = ('whatsapp_link', )

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        if self.model.objects.count() >= 1:
            return False
        return super().has_add_permission(request)


class ContactUsAdmin(admin.ModelAdmin):
    list_display = ('email', 'phone_number', 'subject', 'created', 'updated')
    search_fields = ('email', 'subject', 'first_name', 'last_name', 'message')


class TitledDescriptiveTranslationAdmin(TranslationAdmin):
    ...


admin.site.register(HeaderImage)
admin.site.register(MainInfo, MainInfoAdmin)
admin.site.register(ContactUs, ContactUsAdmin)
admin.site.register(FAQs, TitledDescriptiveTranslationAdmin)
admin.site.register(Works, TitledDescriptiveTranslationAdmin)
admin.site.register(AboutUs, TitledDescriptiveTranslationAdmin)
admin.site.register(CookiePolicy, TitledDescriptiveTranslationAdmin)
admin.site.register(PrivacyPolicy, TitledDescriptiveTranslationAdmin)
admin.site.register(TermsOfService, TitledDescriptiveTranslationAdmin)
