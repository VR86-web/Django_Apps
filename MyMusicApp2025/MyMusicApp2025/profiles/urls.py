from django.urls import path, include

from MyMusicApp2025.profiles import views

urlpatterns = [
    path('details/', views.ProfileDetailsView.as_view(), name='details-profile'),
    path('delete/', views.ProfileDeleteView.as_view(), name='delete-profile'),
]
