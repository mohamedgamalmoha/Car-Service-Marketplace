from modeltranslation.translator import translator, TranslationOptions

from .models import Post


class PostTranslationOptions(TranslationOptions):
    fields = ('title', 'body')


translator.register(Post, PostTranslationOptions)
