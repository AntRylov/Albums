from django.contrib import admin
from .models import Genre, Track, Album, Singer


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ("name", )


@admin.register(Track)
class TrackAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ("title",)


@admin.register(Singer)
class SingerAdmin(admin.ModelAdmin):
    list_display = ("name",)

