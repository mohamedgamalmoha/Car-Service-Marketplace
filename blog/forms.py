from django import forms

from .models import PostComment
from accounts.forms import BaseUpdateCSSClassForm


class PostCommentForm(BaseUpdateCSSClassForm, forms.ModelForm):

    class Meta:
        model = PostComment
        fields = ('title', 'comment')
