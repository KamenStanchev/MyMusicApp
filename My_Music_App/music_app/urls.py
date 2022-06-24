from django.urls import path

from My_Music_App.music_app.views import *

urlpatterns = [
    path('', home_page, name="home_page"),

    path('album/add/', add_album, name='add_album'),
    path('album/details/<id>/', album_details, name='album_details'),
    path('album/edit/<id>/', edit_album, name='edit_album'),
    path('album/delete/<id>/', delete_album, name='delete_album'),

    path('profile/details/', profile_details, name='profile_details'),
    path('profile/delete/', delete_profile, name='delete_profile'),
]
