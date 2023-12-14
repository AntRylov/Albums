import logging
from .decorators import unauthenticated_user
from .forms import CreateUserForm, UpdateProfileForm

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages

from .models import Profile

logger = logging.getLogger('album_logger')


@unauthenticated_user
def login_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            messages.info(request, 'Username or password do not match')
            logger.info('Username or password do not match')
    return render(request, "login.html")


@unauthenticated_user
def register_user(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            try:
                if User.objects.filter(username=username).exists():
                    messages.info(request, f"The user with username {username} already exists")
                else:
                    form.save()
                    messages.info(request, f"The user with username {username} has been registered")
                    return redirect("login")
            except User.DoesNotExist as error:
                logger.error(error)
    context = {
        "form": form
    }
    return render(request, "register.html", context=context)


def logout_user(request):
    logout(request)
    return redirect("home")


def show_user_page(request):
    profile_ = Profile.objects.filter(user__pk=request.user.pk).first()
    context = {
        "profile": profile_
    }
    return render(request, 'profile.html', context=context)


def update_profile(request):
    form = UpdateProfileForm()
    if request.method == "POST":
        form = UpdateProfileForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            profile_ = Profile.objects.filter(user__pk=request.user.pk).first()
            profile_.first_name = data["first_name"]
            profile_.last_name = data["last_name"]
            profile_.bio = data["bio"]
            profile_.avatar = data["avatar"]
            profile_.save()
            messages.success(request, "Profile was updated for " + str(request.user))
            logger.info("Profile was updated for " + str(request.user))
    context = {
        "form": form
    }
    return render(request, "profile_update.html", context=context)