from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from profiles.models import Profile


class CreateUserForm(UserCreationForm):

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class UpdateProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = '__all__'
        exclude = ['user', 'favourites', 'email', 'nickname']

        widgets = {
            'first_name': forms.TextInput(
                attrs={
                 "class": "form-control rounded-4",
                 "style": "max-width: 300px",
                 "placeholder": "Name"
                }),
            'last_name': forms.TextInput(
                attrs={
                 "class": "form-control rounded-4",
                 "style": "max-width: 300px",
                 "placeholder": "Surname"
                }),
            'bio': forms.Textarea(
                attrs={
                 "class": "form-control rounded-4",
                 "style": "max-width: 300px",
                 "placeholder": "My bio"
                }),
            'avatar': forms.FileInput(
                attrs={
                    "class": "form-control rounded-4",
                    "style": "max-width: 300px",
                    "placeholder": "Choose file ..."
                }
            )
        }