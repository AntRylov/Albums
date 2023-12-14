from django.urls import path
from profiles import views


urlpatterns = [
    path('dash/', views.show_user_page, name='user_page'),
    path('dash/update_profile', views.update_profile, name='user_update'),
]