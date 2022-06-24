from django.shortcuts import render, redirect

from My_Music_App.music_app.forms import ProfileForm
from My_Music_App.music_app.models import Profile


def get_profile():
    profile = Profile.objects.all()
    if profile:
        return profile[0]
    return None


def home_page(request):
    profile = get_profile()
    if profile:
        return render(request, 'home-with-profile.html')
    else:
        if request.method == 'POST':
            form = ProfileForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('home_page')
        else:
            form = ProfileForm()
        context = {
            'form': form,
            # 'not_user': True,
        }
        return render(request, 'home-no-profile.html', context)


def add_album(request):
    pass


def album_details(request):
    pass


def edit_album(request):
    pass


def delete_album(request):
    pass


def profile_details(request):
    pass


def delete_profile(request):
    pass
