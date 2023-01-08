from django.db import models
from django import forms

import django_filters

from .models import Post


class PostFilter(django_filters.FilterSet):
    search = django_filters.CharFilter(method='search_filter', label='Search',
                                       widget=forms.widgets.TextInput(attrs={
                                           'type': 'text',
                                           'class': 'form-control shadow-none border-0 text-white py-2 px-2',
                                           'style': "background-color: #222;",
                                           'placeholder': "Search",
                                           'aria-label': "Search",
                                           'aria-describedby': "button-addon2"
                                       }))

    class Meta:
        model = Post
        fields = ('search', )

    def search_filter(self, queryset, name, value):
        return queryset.filter(
            models.Q(title__icontains=value) | models.Q(body__icontains=value)
        )
