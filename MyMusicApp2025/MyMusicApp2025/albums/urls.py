from django.urls import path, include

from MyMusicApp2025.albums import views

urlpatterns = [
    path('add/', views.AlbumAddView.as_view(), name='add-album'),
    path('<int:id>/', include([
        path('edit/', views.AlbumEditView.as_view(), name='edit-album'),
        path('details/', views.AlbumDetailsView.as_view(), name='details-album'),
        path('delete/', views.AlbumDeleteView.as_view(), name='delete-album'),
    ]))

]