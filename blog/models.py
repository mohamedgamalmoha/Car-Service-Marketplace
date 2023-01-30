from django.db import models
from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _

from ckeditor.fields import RichTextField

from accounts.models import Customer


class PostManager(models.Manager):

    def active(self):
        return self.filter(is_active=True)


class Post(models.Model):
    title = models.CharField(verbose_name=_('Title'), max_length=200)
    image = models.ImageField(verbose_name=_('Image'), upload_to='posts/')
    body = RichTextField(verbose_name=_('Body'), null=True)
    is_active = models.BooleanField(verbose_name=_("Activate"), default=True)
    created = models.DateTimeField(verbose_name=_('Created'), auto_now_add=True)
    updated = models.DateTimeField(verbose_name=_('Updated'), auto_now=True)

    objects = PostManager()

    class Meta:
        verbose_name = _('Post')
        verbose_name_plural = _('Posts')

    def show_image(self, width: int = 150, height: int = 100):
        url = self.image.url
        return mark_safe(f'<a href="{url}"> <img src="{url}" width="{width}" height={height} /></a>')
    show_image.short_description = _("Show Image")


class PostComment(models.Model):
    customer = models.ForeignKey(Customer,  on_delete=models.SET_NULL, null=True, related_name='post_comments',
                                 verbose_name=_('Customer'))
    post = models.ForeignKey(Post,  on_delete=models.SET_NULL, null=True, related_name='comments',
                             verbose_name=_('Post'))
    title = models.CharField(max_length=350, null=True, blank=True, verbose_name=_('Title'))
    comment = models.TextField(null=True, blank=True, verbose_name=_('Comment'))
    created = models.DateTimeField(auto_now_add=True, null=False, verbose_name=_('Created'))
    updated = models.DateTimeField(auto_now=True, verbose_name=_('Updated'))

    def __str__(self):
        return self.customer.username

    class Meta:
        verbose_name = _('Comment')
        verbose_name_plural = _('Comments')
