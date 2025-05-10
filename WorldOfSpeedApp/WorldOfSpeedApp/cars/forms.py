from django import forms

from WorldOfSpeedApp.cars.models import Car
from WorldOfSpeedApp.mixins import ReadOnlyMixin


class CarBaseForm(forms.ModelForm):
    class Meta:
        model = Car
        exclude = ['owner',]

        widgets = {
            'type': forms.Select(),
            'model': forms.TextInput(),
            'year': forms.NumberInput(),
            'image_url': forms.URLInput(attrs={
                'placeholder': 'https://...',
            }),
            'price': forms.NumberInput(),
        }

        labels = {
            'type': 'Type:',
            'model': 'Model:',
            'year': 'Year:',
            'image_url': 'Image URL:',
            'price': 'Price:',
        }


class CarCreateForm(CarBaseForm):
    pass


class CarCatalogueForm(CarBaseForm):
    pass


class CarEditForm(CarBaseForm):
    pass


class CarDeleteForm(ReadOnlyMixin, CarBaseForm):
    read_only_fields = ['type', 'model', 'year', 'image_url', 'price',]