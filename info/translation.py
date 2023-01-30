from modeltranslation.translator import translator, TranslationOptions

from .models import MainInfo, FAQs, AboutUs, TermsOfService, Works, CookiePolicy, PrivacyPolicy


class MainInfoTranslationOptions(TranslationOptions):
    fields = ('why_us', )


class FAQsTranslationOptions(TranslationOptions):
    fields = ('quote', 'answer')


class TitledDescriptiveTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


translator.register(FAQs, FAQsTranslationOptions)
translator.register(MainInfo, MainInfoTranslationOptions)
translator.register(Works, TitledDescriptiveTranslationOptions)
translator.register(AboutUs, TitledDescriptiveTranslationOptions)
translator.register(CookiePolicy, TitledDescriptiveTranslationOptions)
translator.register(PrivacyPolicy, TitledDescriptiveTranslationOptions)
translator.register(TermsOfService, TitledDescriptiveTranslationOptions)
