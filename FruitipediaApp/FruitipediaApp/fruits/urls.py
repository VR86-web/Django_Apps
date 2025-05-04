from django.urls import path, include

from FruitipediaApp.fruits import views

urlpatterns = [
    path('create/', views.FruitCreateView.as_view(), name='create-fruit'),
    path('<fruitId>/', include([
        path('details/', views.FruitDetailsView.as_view(), name='details-fruit'),
        path('edit/', views.FruitEditView.as_view(), name='edit-fruit'),
        path('delete/', views.FruitDeleteView.as_view(), name='delete-fruit'),
    ]))
]