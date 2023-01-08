from django.db import models
from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _

from ckeditor.fields import RichTextField

from accounts.models import Customer


class PostManager(models.Manager):

    def active(self):
        return self.filter(is_active=True)


class Post(models.Model):
    title = models.CharField(_('Title'), max_length=200)
    image = models.ImageField(_('Image'), upload_to='posts/')
    body = RichTextField(_('Body'), null=True)
    is_active = models.BooleanField(_("Activate"), default=True)
    created = models.DateTimeField(_('Created'), auto_now_add=True)
    updated = models.DateTimeField(_('Updated'), auto_now=True)

    objects = PostManager()

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def show_image(self, width: int = 150, height: int = 100):
        url = self.image.url
        return mark_safe(f'<a href="{url}"> <img src="{url}" width="{width}" height={height} /></a>')


class PostComment(models.Model):
    customer = models.ForeignKey(Customer,  on_delete=models.SET_NULL, null=True, related_name='post_comments')
    post = models.ForeignKey(Post,  on_delete=models.SET_NULL, null=True, related_name='comments')
    title = models.CharField(max_length=350, null=True, blank=True)
    comment = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, null=False)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.customer.username

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
