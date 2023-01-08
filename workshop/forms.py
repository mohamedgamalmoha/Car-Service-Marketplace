from django import forms

from .models import Rate, Comment, ReportIssue
from accounts.forms import BaseUpdateCSSClassForm


class RateForm(BaseUpdateCSSClassForm, forms.ModelForm):

    class Meta:
        model = Rate
        fields = ('value', )


class CommentForm(BaseUpdateCSSClassForm, forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('title', 'comment')


class ReportIssueForm(BaseUpdateCSSClassForm, forms.ModelForm):

    class Meta:
        model = ReportIssue
        fields = ('title', 'description', 'suggestion', 'attachment', 'date_of_issue')
        widgets = {
            'date_of_issue': forms.widgets.NumberInput(attrs={'type': 'date'})
        }
