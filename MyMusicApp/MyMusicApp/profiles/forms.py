from django import forms

from MyMusicApp.profiles.models import Profile


class ProfileBaseForms(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class ProfileCreateForm(ProfileBaseForms):
    pass
