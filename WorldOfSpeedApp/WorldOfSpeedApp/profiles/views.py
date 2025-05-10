from django.db.models import Sum
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from WorldOfSpeedApp.cars.models import Car
from WorldOfSpeedApp.profiles.forms import ProfileCreateForm, ProfileEditForm
from WorldOfSpeedApp.profiles.models import Profile
from WorldOfSpeedApp.utils import get_user_obj


# Create your views here.


class ProfileCreateView(CreateView):
    model = Profile
    template_name = 'profiles/profile-create.html'
    form_class = ProfileCreateForm
    success_url = reverse_lazy('catalogue-car')


class ProfileDetailsView(DetailView):
    model = Profile
    template_name = 'profiles/profile-details.html'
    context_object_name = 'profile'

    def get_object(self, queryset=None):
        return get_user_obj()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_car_price'] = self.object.cars.aggregate(
            total=Sum('price')
        )['total'] or 0
        return context


class ProfileEditView(UpdateView):
    model = Profile
    template_name = 'profiles/profile-edit.html'
    form_class = ProfileEditForm
    success_url = reverse_lazy('details-profile')

    def get_object(self, queryset=None):
        return get_user_obj()


class ProfileDeleteView(DeleteView):
    model = Profile
    template_name = 'profiles/profile-delete.html'
    success_url = reverse_lazy('index')

    def get_object(self, queryset=None):
        return get_user_obj()