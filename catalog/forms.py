from django import forms
from catalog.models import Album, Singer


class AddAlbum(forms.ModelForm):
    class Meta:
        model = Album
        fields = ["title", "singer", "year", "num_of_tracks", "cover", "genre"]


class SearchForm(forms.Form):
    title = forms.CharField(max_length=100)
