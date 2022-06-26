from django.shortcuts import render, redirect

from My_Music_App.music_app.forms import ProfileForm, AlbumForm
from My_Music_App.music_app.models import Profile, Album


def get_profile():
    profile = Profile.objects.all()
    if profile:
        return profile[0]
    return None


def home_page(request):
    profile = get_profile()
    if profile:
        albums = Album.objects.all()
        context = {
            'albums': albums,
        }
        return render(request, 'home-with-profile.html', context)
    else:
        if request.method == 'POST':
            form = ProfileForm(request.POST)
            if form.is_valid():
                purchase = form.save(commit=False)
                if purchase.image is None:
                    purchase.image = 'https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_960_720.png'
                purchase.save()
                return redirect('home_page')
        else:
            form = ProfileForm()
        context = {
            'form': form,
            'not_user': True,
        }
        return render(request, 'home-no-profile.html', context)


def add_album(request):
    if request.method == 'POST':
        form = AlbumForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home_page')
    else:
        form = AlbumForm()
    context = {
        'form': form,
    }
    return render(request, 'add-album.html', context)


def album_details(request, id):
    album = Album.objects.get(id=id)
    context = {
        'album': album,
    }
    return render(request, 'album-details.html', context)


def edit_album(request, id):
    album = Album.objects.get(id=id)
    if request.method == 'POST':
        form = AlbumForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('home_page')
    else:
        form = AlbumForm(instance=album)
    context = {
        'form': form,
        'id': id,
    }
    return render(request, 'edit-album.html', context)


def delete_album(request, id):
    album = Album.objects.get(id=id)
    form = AlbumForm(instance=album)
    for field in form.fields:
        form.fields[field].disabled = True
    if request.method == 'POST':
        album.delete()
        return redirect('home_page')
    context = {
        'form': form,
        'id': id,

    }
    return render(request, 'delete-album.html', context)


def profile_details(request):
    profile = get_profile()
    albums = Album.objects.all()
    albums_count = len(albums)
    context = {
        'profile': profile,
        'albums_count': albums_count,
    }
    return render(request, 'profile-details.html', context)


def edit_profile(request):
    profile = get_profile()
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile_details')
    else:
        form = ProfileForm(instance=profile)
    context = {'form': form, 'profile': profile}
    return render(request, 'edit-profile.html', context)


def delete_profile(request):
    profile = get_profile()
    if request.method == "POST":
        albums = Album.objects.all()
        for i in range(len(albums)-1, -1, -1):
            album = albums[i]
            album.delete()

        profile.delete()
        return redirect('home_page')

    return render(request, 'profile-delete.html')
