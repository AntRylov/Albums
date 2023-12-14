from django.contrib import admin
from django.utils.safestring import mark_safe

from profiles.models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ["id", "email"]
    readonly_fields = ["get_image"]

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.avatar.url} width="100" height="110">')

    get_image.short_description = "Avatar"
