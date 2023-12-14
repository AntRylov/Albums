import logging
from django.http import HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from catalog.models import Album, Singer, Genre

logger = logging.getLogger('album_logger')


def index(request):
    logger.info("Start application")
    return render(request, "base.html")


def catalog_view(request):
    albums = Album.objects.defer(
        'title',
        'year',
        'genre',
        'created_at',
        'updated_at'
    )
    context = {
        "albums": albums
    }
    return render(request, "albums.html", context=context)


def album_detail_view(request, album_slug):
    album = Album.objects.prefetch_related().get(slug=album_slug)
    genres = Genre.objects.all()
    singers = Singer.objects.all()
    context = {
        "album": album,
        "genres": genres,
        "singers": singers

    }
    return render(request, 'album.html', context=context)


def favourite_add(request, album_id):
    album = Album.objects.get(id=album_id)
    profile = request.user.profile_user
    if profile.favourites.filter(id=album_id).exists():
        profile.favourites.remove(album)
    else:
        profile.favourites.add(album)
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


def favourite_list(request):
    f_albums = request.user.profile_user.favourites.all()
    context = {
        "f_albums": f_albums
    }
    return render(request, 'favourites.html', context=context)


def pageNotFound(request, exception):
    return HttpResponseNotFound("<h3>Page not found</h3>")

