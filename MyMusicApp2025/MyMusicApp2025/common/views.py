
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import BaseFormView

from MyMusicApp2025.albums.models import Album
from MyMusicApp2025.profiles.forms import ProfileCreateForm
from MyMusicApp2025.utils import get_user_obj


# Create your views here.


class HomePageView(ListView, BaseFormView):
    model = Album
    form_class = ProfileCreateForm
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['profile'] = get_user_obj()
        return context

    def get_template_names(self):
        profile = get_user_obj()

        if profile:
            return ['common/home-with-profile.html']
        else:
            return ['common/home-no-profile.html']
        
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
