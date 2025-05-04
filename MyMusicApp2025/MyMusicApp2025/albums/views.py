from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView, FormView

from MyMusicApp2025.albums.forms import AlbumAddForm, AlbumEditForm, AlbumDeleteForm
from MyMusicApp2025.albums.models import Album
from MyMusicApp2025.utils import get_user_obj


# Create your views here.


class AlbumAddView(CreateView):
    model = Album
    template_name = 'albums/album-add.html'
    form_class = AlbumAddForm
    success_url = reverse_lazy('home')
    
    def form_valid(self, form):
        form.instance.owner = get_user_obj()

        return super().form_valid(form)


class AlbumEditView(UpdateView):
    model = Album
    template_name = 'albums/album-edit.html'
    success_url = reverse_lazy('home')
    form_class = AlbumEditForm
    pk_url_kwarg = 'id'


class AlbumDetailsView(DetailView):
    model = Album
    template_name = 'albums/album-details.html'
    pk_url_kwarg = 'id'


class AlbumDeleteView(DeleteView):
    model = Album
    template_name = 'albums/album-delete.html'
    success_url = reverse_lazy('home')
    form_class = AlbumDeleteForm
    pk_url_kwarg = 'id'

    def get_initial(self):
        return self.object.__dict__

    def form_invalid(self, form):
        return self.form_valid(form)



