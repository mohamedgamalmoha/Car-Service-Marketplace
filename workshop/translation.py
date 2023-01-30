from modeltranslation.translator import translator, TranslationOptions

from .models import Service, WorkShop, WorkShopLocation, WorkShopVideo


class ServiceTranslationOptions(TranslationOptions):
    fields = ('name', 'description')


class WorkshopTranslationOptions(TranslationOptions):
    fields = ('name', 'description')


class WorkShopLocationTranslationOptions(TranslationOptions):
    fields = ('address', )


class WorkShopVideoTranslationOptions(TranslationOptions):
    fields = ('title',)


translator.register(Service, ServiceTranslationOptions)
translator.register(WorkShop, WorkshopTranslationOptions)
translator.register(WorkShopVideo, WorkShopVideoTranslationOptions)
translator.register(WorkShopLocation, WorkShopLocationTranslationOptions)
