from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from TastyRecipesApp.profiles.forms import ProfileCreateForm, ProfileEditForm
from TastyRecipesApp.profiles.models import Profile
from TastyRecipesApp.utils import get_user_obj


class CreateProfileView(CreateView):
    model = Profile
    template_name = 'profiles/create-profile.html'
    form_class = ProfileCreateForm
    success_url = reverse_lazy('catalogue-recipes')


class DetailsProfileView(DetailView):
    model = Profile
    template_name = 'profiles/details-profile.html'

    def get_object(self, queryset=None):
        return get_user_obj()


class EditProfileView(UpdateView):
    model = Profile
    template_name = 'profiles/edit-profile.html'
    success_url = reverse_lazy('details-profile')
    form_class = ProfileEditForm

    def get_object(self, queryset=None):
        return get_user_obj()


class DeleteProfileView(DeleteView):
    model = Profile
    template_name = 'profiles/delete-profile.html'
    success_url = reverse_lazy('home')

    def get_object(self, queryset=None):
        return get_user_obj()

