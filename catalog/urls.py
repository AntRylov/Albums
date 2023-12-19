from django.urls import path
from catalog import views

urlpatterns = [
    path('', views.catalog_view, name='albums_list'),
    path('fav/<int:album_id>', views.favourite_add, name='favourite'),
    path('favourites/', views.favourite_list, name='favourite_list'),
    path('<slug:album_slug>', views.album_detail_view, name='album_details'),
    path('add/', views.add_album, name='add_album'),
    path('search/', views.search_result, name='search_album'),
    path('delete/<int:get_album>', views.album_delete, name='delete_album'),
    path('edit/<int:album_id>', views.edit_album, name='edit_album'),
    ]
