from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from FruitipediaApp.fruits.forms import FruitBaseForm
from FruitipediaApp.fruits.models import Fruit
from FruitipediaApp.utils import get_user_obj


# Create your views here.


class IndexPage(TemplateView):
    template_name = 'common/index.html'


class DashboardPage(ListView):
    model = Fruit
    template_name = 'common/dashboard.html'
    context_object_name = 'fruits'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['form'] = FruitBaseForm
        return context
