import logging
from django.http import HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render, redirect
from catalog.models import Album, Singer, Genre, Track
from catalog.forms import AddAlbum, SearchForm


logger = logging.getLogger('album_logger')


def index(request):
    logger.info("Start application")
    return render(request, "base.html")


def catalog_view(request):
    albums = Album.objects.defer(
        'title',
        'year',
        'genre',
        'num_of_tracks',
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


def search_result(request):
    query = request.GET.get('q')
    albums = Album.objects.filter(title__icontains=query)
    context = {
        'albums': albums
    }

    return render(request, "search_res.html", context=context)


def favourite_list(request):
    f_albums = request.user.profile_user.favourites.all()
    context = {
        "f_albums": f_albums
    }
    return render(request, 'favourites.html', context=context)


def add_album(request):
    form = AddAlbum
    if request.method == "POST":
        form = AddAlbum(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.singer = request.user
            obj.save()
            logger.info(f"Album {obj.title} created by {request.user}")
            return redirect('albums')
    context = {
        'form': form
    }
    return render(request, "add_album.html", context=context)


def album_delete(request, get_album):
    album = Album.objects.get(id=get_album)
    album.delete()
    logger.info(f"Album by {album.singer} removed {album.title}")
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


def edit_album(request, album_id):
    form = Album.objects.get(id=album_id)
    form_ = AddAlbum(request.POST, instance=form)
    if request.method == "POST":
        if form_.is_valid():
            obj = form_.save(commit=False)
            obj.singer = request.user
            obj.save()
            form_.save_m2m()
            logger.info(f"Album {obj.title} edited {request.user}")
            return redirect('albums')
    context = {
        'form': form_
    }
    return render(request, "edit_album.html", context=context)


def pageNotFound(request, exception):
    return HttpResponseNotFound("<h3>Page not found</h3>")

