
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import BaseFormView

from MyMusicApp.album.models import Album
from MyMusicApp.profiles.forms import ProfileCreateForm
from MyMusicApp.utils import get_user_object


# Create your views here.

class HomePage(ListView, BaseFormView):
    model = Album
    form_class = ProfileCreateForm
    success_url = reverse_lazy('home')

    def get_template_names(self):
        profile = get_user_object()

        if profile:
            return ['profiles/home-with-profile.html']

        return ['profiles/home-no-profile.html']

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)