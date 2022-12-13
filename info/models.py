from django.db import models
from accounts.models import PhoneNumberValidator


class MainInfo(models.Model):
    facebook = models.URLField('Facebook link')
    instagram = models.URLField('Instagram link')
    twitter = models.URLField('Twitter link')
    telegram = models.URLField('Telegram link', blank=True, null=True)
    open_at = models.TimeField(null=True)
    close_at = models.TimeField(null=True)
    mail = models.EmailField('Web email')
    whatsapp = models.CharField("Whatsapp number", max_length=11, validators=[PhoneNumberValidator, ])

    class Meta:
        verbose_name = 'Website Main Info'
        verbose_name_plural = 'Website Main Info'

    def __str__(self):
        return self.mail

    @property
    def whatsapp_link(self):
        return f"https://wa.me/+2{self.whatsapp}"


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


class ContactUs(models.Model):
    first_name = models.CharField(max_length=120, null=True)
    last_name = models.CharField(max_length=120, null=True)
    email = models.EmailField()
    phone_number = models.CharField(max_length=11, validators=[PhoneNumberValidator, ], null=True)
    subject = models.CharField(max_length=250)
    message = models.TextField()
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        verbose_name = 'Contact Us'
        verbose_name_plural = 'Contact Us'
