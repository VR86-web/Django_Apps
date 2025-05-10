from django.urls import path, include

from WorldOfSpeedApp.cars import views

urlpatterns = [
    path('create/', views.CarCreateView.as_view(), name='create-car'),
    path('catalogue/', views.CarCatalogueView.as_view(), name='catalogue-car'),
    path('<id>/', include([
        path('details/', views.CarDetailsView.as_view(), name='details-car'),
        path('edit/', views.CarEditView.as_view(), name='edit-car'),
        path('delete/', views.CarDeleteView.as_view(), name='delete-car'),
    ]))
]