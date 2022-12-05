from django.db import models
from accounts.models import PhoneNumberValidator


class MainInfo(models.Model):
    facebook = models.URLField('Facebook link')
    instagram = models.URLField('Instagram link')
    twitter = models.URLField('Twitter link')
    telegram = models.URLField('Telegram link', blank=True, null=True)

    mail = models.EmailField('Web email')
    whatsapp = models.CharField("Whatsapp number", max_length=11, validators=[PhoneNumberValidator, ])

    class Meta:
        verbose_name = 'Website Main Info'
        verbose_name_plural = 'Website Main Info'

    def __str__(self):
        return self.mail


class FAQs(models.Model):
    quote = models.CharField(max_length=1000)
    answer = models.TextField()

    class Meta:
        verbose_name = 'FAQ'
        verbose_name_plural = 'FAQs'

    def __str__(self):
        return self.quote


class AboutUs(models.Model):
    title = models.CharField(max_length=500)
    description = models.TextField()

    class Meta:
        verbose_name = 'About us'
        verbose_name_plural = 'About us'

    def __str__(self):
        return self.title


class TermsOfService(models.Model):
    title = models.CharField(max_length=500)
    description = models.TextField()

    class Meta:
        verbose_name = 'Terms Of Service'
        verbose_name_plural = 'Terms Of Service'

    def __str__(self):
        return self.title


class Works(models.Model):
    title = models.CharField(max_length=500)
    description = models.TextField()

    class Meta:
        verbose_name = 'How it works'
        verbose_name_plural = 'How it works'

    def __str__(self):
        return self.title


class CookiePolicy(models.Model):
    title = models.CharField(max_length=500)
    description = models.TextField()

    class Meta:
        verbose_name = 'Cookie Policy'
        verbose_name_plural = 'Cookie Policy'

    def __str__(self):
        return self.title


class PrivacyPolicy(models.Model):
    title = models.CharField(max_length=500)
    description = models.TextField()

    class Meta:
        verbose_name = 'Privacy Policy'
        verbose_name_plural = 'Privacy Policy'

    def __str__(self):
        return self.title
