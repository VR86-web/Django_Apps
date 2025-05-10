from django import forms

from WorldOfSpeedApp.profiles.models import Profile


class ProfileBaseForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['username', 'email', 'age', 'password',]

        widgets = {
            'username': forms.TextInput(),
            'email': forms.EmailInput(),
            'age': forms.NumberInput(),
            'password': forms.PasswordInput(),
        }

        labels = {
            'username': 'Username:',
            'email': 'Email:',
            'age': 'Age:',
            'password': 'Password:',
        }

        help_texts = {
            'age': 'Age requirement: 21 years and above.',
        }


class ProfileCreateForm(ProfileBaseForm):
    pass


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            'username',
            'email',
            'age',
            'password',
            'first_name',
            'last_name',
            'profile_picture',
        ]

        widgets = {
            'password': forms.PasswordInput(render_value=True),
        }

        labels = {
            'username': 'Username:',
            'email': 'Email:',
            'age': 'Age:',
            'password': 'Password:',
            'first_name': 'First Name:',
            'last_name': 'Last Name:',
            'profile_picture': 'Profile Picture:',
        }



