from django.urls import path

from MyMusicApp.common import views

urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
]