from django.urls import path

from FruitipediaApp.common import views

urlpatterns = [
    path('', views.IndexPage.as_view(), name='index'),
    path('dashboard/', views.DashboardPage.as_view(), name='dashboard')
]