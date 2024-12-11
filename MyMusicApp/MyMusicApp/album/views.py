from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView

from MyMusicApp.album.forms import AlbumCreateForm, AlbumEditForm, AlbumDeleteForm
from MyMusicApp.album.models import Album
from MyMusicApp.utils import get_user_object


# Create your views here.


class AlbumCreateView(CreateView):
    model = Album
    form_class = AlbumCreateForm
    template_name = 'albums/album-add.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.owner = get_user_object()
        return super().form_valid(form)


class AlbumEditView(UpdateView):
    model = Album
    form_class = AlbumEditForm
    pk_url_kwarg = 'id'
    template_name = 'albums/album-edit.html'
    success_url = reverse_lazy('home')


class AlbumDetailsView(DetailView):
    model = Album
    template_name = 'albums/album-details.html'
    pk_url_kwarg = 'id'



class AlbumDeleteView(DeleteView):
    model = Album
    pk_url_kwarg = 'id'
    template_name = 'albums/album-delete.html'
    success_url = reverse_lazy('home')
    form_class = AlbumDeleteForm

    def get_initial(self):
        return self.object.__dict__

    def form_invalid(self, form):
        return self.form_valid(form)
