from django import forms

from My_Music_App.music_app.models import Profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('username', 'email', 'age')

        widgets = {
            'username': forms.TextInput(
                attrs={
                    'placeholder': 'Username'
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'placeholder': 'Email'
                }
            ),

            'age': forms.NumberInput(
                attrs={
                    'placeholder': 'Age'
                }
            )
        }


# class AlbumForm(forms.ModelForm):
#     class Meta:
#         model = Album
#         fields = '__all__'
