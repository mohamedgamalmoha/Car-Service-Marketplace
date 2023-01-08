from django import forms

from .models import Car
from accounts.forms import BaseUpdateCSSClassForm


class CarForm(BaseUpdateCSSClassForm, forms.ModelForm):

    # def __init__(self, *args, **kw):
    #     super(CarForm, self).__init__(*args, **kw)
    #     del self.fields['color'].widget.attrs['class']

    class Meta:
        model = Car
        exclude = ('customer', 'created', 'updated')
        widgets = {
            'color': forms.widgets.TextInput(attrs={'type': 'color', 'class': ''}),
        }
