from django.urls import path

from MyMusicApp2025.common import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
]