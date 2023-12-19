from django.db import models
from django.urls import reverse
from PIL import Image


class Genre(models.Model):
    name = models.CharField('Name of genre', max_length=50, null=False, blank=False)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Genre"
        verbose_name_plural = "Genres"


class Track(models.Model):
    name = models.CharField(max_length=40)
    duration = models.CharField(max_length=4, verbose_name="Duration of track")
    text = models.TextField(verbose_name="Text of track", null=True, blank=True)

    created_at = models.DateTimeField(verbose_name="Created at", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="Updated at", auto_now=True)

    def __str__(self):
        return f"{self.pk} - {self.name}"

    class Meta:
        verbose_name = "Track"
        verbose_name_plural = "Tracks"


class Singer(models.Model):
    name = models.CharField(max_length=30, verbose_name="Singer name")
    bio = models.TextField(verbose_name="biography")
    photo = models.ImageField(verbose_name="Image", default="default.png", upload_to='albums/')
    slug = models.SlugField(unique=True, db_index=True, verbose_name="URL")

    created_at = models.DateTimeField(verbose_name="Created at", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="Updated at", auto_now_add=True)

    def __str__(self):
        return f"{self.pk} - {self.name}"

    def get_absolute_url(self):
        return reverse("singer_view", kwargs={"singer_slug": self.slug})

    class Meta:
        verbose_name = "Singer"
        verbose_name_plural = "Singers"
        ordering = ['name']


class Album(models.Model):
    singer = models.OneToOneField(Singer, related_name="album_singer", on_delete=models.CASCADE)
    title = models.CharField(max_length=40, verbose_name="Title")
    year = models.PositiveSmallIntegerField(verbose_name="Year of production")
    num_of_tracks = models.IntegerField(verbose_name="Number of tracks")
    duration = models.CharField(max_length=5, verbose_name="Duration of album")
    cover = models.ImageField("Cover", default="cover.png", upload_to='albums/')
    track = models.ManyToManyField(Track, related_name="album_track")
    slug = models.SlugField(unique=True)
    genre = models.ForeignKey(Genre, related_name="album_genre", on_delete=models.CASCADE)

    created_at = models.DateTimeField(verbose_name="Created at", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="Updated at", auto_now=True)

    def __str__(self):
        return f"{self.pk} - {self.title}"

    def get_absolute_url(self):
        return reverse("album_detail_view", kwargs={"album_slug": self.slug})

    class Meta:
        verbose_name = "Album"
        verbose_name_plural = "Albums"
        ordering = ['year']
        indexes = [
            models.Index(fields=('created_at',))
        ]

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.cover.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.cover.path)
