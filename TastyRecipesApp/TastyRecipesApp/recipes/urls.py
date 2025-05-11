from django.urls import path, include

from TastyRecipesApp.recipes import views

urlpatterns = [
    path('create/', views.CreateRecipeView.as_view(), name='create-recipe'),
    path('catalogue/', views.CatalogueRecipeView.as_view(), name='catalogue-recipes'),
    path('<recipe_id>/', include([
        path('details/', views.DetailsRecipeView.as_view(), name='details-recipe'),
        path('edit/', views.EditRecipeView.as_view(), name='edit-recipe'),
        path('delete/', views.DeleteRecipeView.as_view(), name='delete-recipe'),
    ]))
]