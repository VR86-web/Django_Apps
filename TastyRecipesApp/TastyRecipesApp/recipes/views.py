
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

from TastyRecipesApp.recipes.forms import RecipeCreateForm, RecipeBaseForm, RecipeEditForm, RecipeDeleteForm
from TastyRecipesApp.recipes.models import Recipe
from TastyRecipesApp.utils import get_user_obj


# Create your views here.


class CreateRecipeView(CreateView):
    model = Recipe
    template_name = 'recipes/create-recipe.html'
    form_class = RecipeCreateForm
    success_url = reverse_lazy('catalogue-recipes')

    def form_valid(self, form):
        form.instance.author = get_user_obj()

        return super().form_valid(form)


class CatalogueRecipeView(ListView):
    model = Recipe
    template_name = 'recipes/catalogue.html'
    context_object_name = 'recipes'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['form'] = RecipeBaseForm
        return context


class DetailsRecipeView(DetailView):
    model = Recipe
    template_name = 'recipes/details-recipe.html'
    pk_url_kwarg = 'recipe_id'
    context_object_name = 'recipe'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        recipe = self.get_object()
        context['ingredient_list'] = [i.strip() for i in recipe.ingredients.split(',')] if recipe.ingredients else []
        return context


class EditRecipeView(UpdateView):
    model = Recipe
    template_name = 'recipes/edit-recipe.html'
    pk_url_kwarg = 'recipe_id'
    success_url = reverse_lazy('catalogue-recipes')
    form_class = RecipeEditForm
    context_object_name = 'recipe'


class DeleteRecipeView(DeleteView):
    model = Recipe
    template_name = 'recipes/delete-recipe.html'
    success_url = reverse_lazy('catalogue-recipes')
    form_class = RecipeDeleteForm
    context_object_name = 'recipe'
    pk_url_kwarg = 'recipe_id'

    def form_invalid(self, form):
        return self.form_valid(form)

    def get_initial(self, **kwargs):
        return self.object.__dict__
