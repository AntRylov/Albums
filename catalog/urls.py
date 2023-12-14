from django.urls import path
from catalog import views

urlpatterns = [
    path('', views.catalog_view, name='albums_list'),
    path('fav/<int:album_id>', views.favourite_add, name='favourite'),
    path('favourites/', views.favourite_list, name='favourite_list'),
    path('<slug:album_slug>', views.album_detail_view, name='album_details')
    ,
]