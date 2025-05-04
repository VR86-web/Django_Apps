from django import forms

from MyMusicApp2025.mixins import PlaceholderMixin
from MyMusicApp2025.profiles.models import Profile


class ProfileBaseForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class ProfileCreateForm(PlaceholderMixin, ProfileBaseForm):
    pass


class ProfileDetailsForm(ProfileBaseForm):
    pass


class ProfileDeleteForm(ProfileBaseForm):
    pass
