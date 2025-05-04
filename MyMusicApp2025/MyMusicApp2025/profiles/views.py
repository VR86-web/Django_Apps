from django.urls import reverse_lazy
from django.views.generic import DetailView, DeleteView

from MyMusicApp2025.profiles.models import Profile
from MyMusicApp2025.utils import get_user_obj


class ProfileDetailsView(DetailView):
    template_name = 'profiles/profile-details.html'

    def get_object(self, queryset=None):

        return get_user_obj()


class ProfileDeleteView(DeleteView):
    success_url = reverse_lazy('home')
    template_name = 'profiles/profile-delete.html'

    def get_object(self, queryset=None):

        return get_user_obj()