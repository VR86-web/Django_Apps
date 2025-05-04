from django import forms

from FruitipediaApp.profiles.models import Profile


class ProfileBaseForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['age', 'image_url',]

        widgets = {
            'first_name': forms.TextInput(attrs={
                'placeholder': 'First Name',
            }),
            'last_name': forms.TextInput(attrs={
                'placeholder': 'Last Name',
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'Email',
            }),
            'password': forms.PasswordInput(attrs={
                'placeholder': 'Password',
            }),
        }
        labels = {
            'first_name': '',
            'last_name': '',
            'email': '',
            'password': '',
        }
        help_texts = {
            'password': '*Password length requirements: 8 to 20 characters',
        }


class ProfileCreateForm(ProfileBaseForm):
    pass


class ProfileDetailsForm(ProfileBaseForm):
    pass


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'image_url', 'age']

        labels = {
            'first_name': 'First Name:',
            'last_name': 'Last Name:',
            'image_url': 'Image URL:',
            'age': 'Age:',
        }