from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from FruitipediaApp.profiles.forms import ProfileCreateForm, ProfileEditForm
from FruitipediaApp.profiles.models import Profile
from FruitipediaApp.utils import get_user_obj


# Create your views here.


class ProfileCreateView(CreateView):
    model = Profile
    template_name = 'profiles/create-profile.html'
    success_url = reverse_lazy('dashboard')
    form_class = ProfileCreateForm


class ProfileDetailsView(DetailView):
    template_name = 'profiles/details-profile.html'

    def get_object(self, queryset=None):
        return get_user_obj()


class ProfileEditView(UpdateView):
    model = Profile
    template_name = 'profiles/edit-profile.html'
    success_url = reverse_lazy('details-profile')
    form_class = ProfileEditForm

    def get_object(self, queryset=None):
        return get_user_obj()


class ProfileDeleteView(DeleteView):
    model = Profile
    template_name = 'profiles/delete-profile.html'
    success_url = reverse_lazy('index')

    def get_object(self, queryset=None):
        return get_user_obj()