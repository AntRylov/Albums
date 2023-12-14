from django.db import models
from django.contrib.auth.models import User

from catalog.models import Album


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile_user")
    first_name = models.CharField("First name", max_length=50)
    last_name = models.CharField("Last name", max_length=50)
    nickname = models.CharField("Nickname", max_length=50, null=True, blank=True)
    email = models.EmailField("Email", max_length=100, null=True, blank=True)
    bio = models.TextField("Biography", max_length=500, null=True, blank=True)
    avatar = models.ImageField("Avatar", upload_to="users/", default="default.png")
    favourites = models.ManyToManyField(Album, blank=True, default=None, related_name="favourite_album")

    created_at = models.DateTimeField(verbose_name="Created at", auto_now_add=True, null=True)
    updated_at = models.DateTimeField(verbose_name="Updated at", auto_now=True, null=True)

    def __str__(self):
        return f"{self.pk} - {self.user.username}"

    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"

        