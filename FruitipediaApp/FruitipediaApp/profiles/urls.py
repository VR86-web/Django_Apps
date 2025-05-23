from django.urls import path

from FruitipediaApp.profiles import views

urlpatterns = [
    path('create/', views.ProfileCreateView.as_view(), name='create-profile'),
    path('details/', views.ProfileDetailsView.as_view(), name='details-profile'),
    path('edit/', views.ProfileEditView.as_view(), name='edit-profile'),
    path('delete/', views.ProfileDeleteView.as_view(), name='delete-profile'),
]