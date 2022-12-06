from django import forms

from .models import Rate, Comment, ReportIssue


class RateForm(forms.ModelForm):

    class Meta:
        model = Rate
        fields = ('value', )


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('title', 'comment')


class ReportIssueForm(forms.ModelForm):

    class Meta:
        model = ReportIssue
        fields = ('title', 'description', 'suggestion', 'attachment', 'date_of_issue')
