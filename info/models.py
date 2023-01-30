from django.db import models
from django.utils.translation import gettext_lazy as _

from accounts.models import PhoneNumberValidator


class MainInfo(models.Model):
    facebook = models.URLField(verbose_name=_('Facebook Link'))
    instagram = models.URLField(verbose_name=_('Instagram Link'))
    twitter = models.URLField(verbose_name=_('Twitter Link'))
    telegram = models.URLField(verbose_name=_('Telegram Link'), blank=True, null=True)
    open_at = models.TimeField(verbose_name=_('Open At'), null=True)
    close_at = models.TimeField(verbose_name=_('Close At'), null=True)
    mail = models.EmailField(verbose_name=_('Web Email'))
    whatsapp = models.CharField(verbose_name=_("Whatsapp Number"), max_length=11, validators=[PhoneNumberValidator, ])
    why_us = models.TextField(verbose_name=_("Why do you choose us?"), null=True)

    class Meta:
        verbose_name = _('Website Main Info')
        verbose_name_plural = _('Website Main Info')

    def __str__(self):
        return self.mail

    def whatsapp_link(self):
        return f"https://wa.me/+2{self.whatsapp}"
    whatsapp_link.short_description = _("Whatsapp Link")


class FAQs(models.Model):
    quote = models.CharField(verbose_name=_("Quote"), max_length=1000)
    answer = models.TextField(verbose_name=_("Answer"))

    class Meta:
        verbose_name = _('FAQ')
        verbose_name_plural = _('FAQs')

    def __str__(self):
        return self.quote


class AboutUs(models.Model):
    title = models.CharField(verbose_name=_("Title"), max_length=500)
    description = models.TextField(verbose_name=_("Description"))

    class Meta:
        verbose_name = _('About us')
        verbose_name_plural = _('About us')

    def __str__(self):
        return self.title


class TermsOfService(models.Model):
    title = models.CharField(verbose_name=_("Title"), max_length=500)
    description = models.TextField(verbose_name=_("Description"))

    class Meta:
        verbose_name = _('Terms Of Service')
        verbose_name_plural = _('Terms Of Service')

    def __str__(self):
        return self.title


class Works(models.Model):
    title = models.CharField(verbose_name=_("Title"), max_length=500)
    description = models.TextField(verbose_name=_("Description"))

    class Meta:
        verbose_name = _('How it works')
        verbose_name_plural = _('How it works')

    def __str__(self):
        return self.title


class CookiePolicy(models.Model):
    title = models.CharField(verbose_name=_("Title"), max_length=500)
    description = models.TextField(verbose_name=_("Description"))

    class Meta:
        verbose_name = _('Cookie Policy')
        verbose_name_plural = _('Cookie Policy')

    def __str__(self):
        return self.title


class PrivacyPolicy(models.Model):
    title = models.CharField(verbose_name=_("Title"), max_length=500)
    description = models.TextField(verbose_name=_("Description"))

    class Meta:
        verbose_name = _('Privacy Policy')
        verbose_name_plural = _('Privacy Policy')

    def __str__(self):
        return self.title


class ContactUs(models.Model):
    first_name = models.CharField(verbose_name=_("First Name"), max_length=120, null=True)
    last_name = models.CharField(verbose_name=_("Last name"), max_length=120, null=True)
    email = models.EmailField(verbose_name=_("Email"))
    phone_number = models.CharField(verbose_name=_("Phone Number"), max_length=11, validators=[PhoneNumberValidator, ], null=True)
    subject = models.CharField(verbose_name=_("Subject"), max_length=250)
    message = models.TextField(verbose_name=_("Message"))
    created = models.DateTimeField(verbose_name=_("Created"), auto_now_add=True, null=True)
    updated = models.DateTimeField(verbose_name=_("Updated"), auto_now=True, null=True)

    class Meta:
        verbose_name = _('Contact Us')
        verbose_name_plural = _('Contact Us')


class HeaderImageManager(models.Manager):

    def active(self):
        return self.filter(active=True)


class HeaderImage(models.Model):
    alt = models.CharField(verbose_name=_("Alternative (Alt)"), max_length=250, help_text=_("Text is meant to convey the “why” of the image as it relates to the content of a document or webpage"))
    image = models.ImageField(upload_to='home/header', verbose_name=_("Image"))
    active = models.BooleanField(default=True, help_text=_("Setting it to false, makes the image disappear from homepage"),
                                 verbose_name=_("Active"))

    objects = HeaderImageManager()

    def __str__(self):
        return self.alt

    class Meta:
        verbose_name = _('Home Page Image')
        verbose_name_plural = _('Home Page Images')
