from django import forms

from FruitipediaApp.fruits.models import Fruit
from FruitipediaApp.mixins import ReadOnlyMixin


class FruitBaseForm(forms.ModelForm):
    class Meta:
        model = Fruit
        fields = ['name', 'image_url', 'description', 'nutrition']

        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Fruit Name',
            }),
            'image_url': forms.URLInput(attrs={
                'placeholder': 'Fruit Image URL',
            }),
            'description': forms.TextInput(attrs={
                'placeholder': 'Fruit Description',
            }),
            'nutrition': forms.TextInput(attrs={
                'placeholder': 'Nutrition Info',
            }),
        }
        labels = {
            'name': '',
            'image_url': '',
            'description': '',
            'nutrition': '',
        }


class FruitCreateForm(FruitBaseForm):
    pass


class FruitEditForm(FruitBaseForm):
    pass


class FruitDeleteForm(ReadOnlyMixin, FruitBaseForm):
    read_only_fields = ['name', 'image_url', 'description', 'nutrition']


