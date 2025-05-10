from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

from WorldOfSpeedApp.cars.forms import CarCreateForm, CarCatalogueForm, CarEditForm, CarDeleteForm
from WorldOfSpeedApp.cars.models import Car
from WorldOfSpeedApp.utils import get_user_obj


# Create your views here.


class CarCreateView(CreateView):
    model = Car
    template_name = 'cars/car-create.html'
    form_class = CarCreateForm
    success_url = reverse_lazy('catalogue-car')

    def form_valid(self, form):
        form.instance.owner = get_user_obj()

        return super().form_valid(form)


class CarCatalogueView(ListView):
    model = Car
    template_name = 'common/../../templates/cars/catalogue.html'
    context_object_name = 'cars'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['form'] = CarCatalogueForm
        return context


class CarDetailsView(DetailView):
    model = Car
    template_name = 'cars/car-details.html'
    pk_url_kwarg = 'id'
    context_object_name = 'car'


class CarEditView(UpdateView):
    model = Car
    template_name = 'cars/car-edit.html'
    pk_url_kwarg = 'id'
    form_class = CarEditForm
    success_url = reverse_lazy('catalogue-car')

    def form_valid(self, form):
        form.instance.owner = get_user_obj()

        return super().form_valid(form)


class CarDeleteView(DeleteView):
    model = Car
    template_name = 'cars/car-delete.html'
    success_url = reverse_lazy('catalogue-car')
    form_class = CarDeleteForm
    pk_url_kwarg = 'id'

    def get_initial(self):
        return self.object.__dict__

    def form_invalid(self, form):
        return self.form_valid(form)

