from django import forms

from TastyRecipesApp.profiles.models import Profile


class ProfileBaseForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['nickname', 'first_name', 'last_name', 'chef']

        labels = {
            'nickname': 'Nickname:',
            'first_name': 'First Name:',
            'last_name': 'Last Name:',
            'chef': 'Chef:',
        }

        widgets = {
            'chef': forms.CheckboxInput(),
        }


class ProfileCreateForm(ProfileBaseForm):
    pass


class ProfileEditForm(ProfileBaseForm):
    class Meta(ProfileBaseForm.Meta):
        fields = ProfileBaseForm.Meta.fields + ['bio',]
        labels = {**ProfileBaseForm.Meta.labels, 'bio': 'Bio:'}


