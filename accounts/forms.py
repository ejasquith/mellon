from django import forms
from django.contrib.auth.forms import UserChangeForm
from .models import CustomUser


class CustomUserChangeForm(UserChangeForm):
    display_name = forms.CharField(label="display_name", required=False)
    bio = forms.CharField(widget=forms.Textarea, required=False)
    profile_picture = forms.ImageField(label="profile_picture", required=False)

    class Meta():
        model = CustomUser
        fields = ("username", "email", "display_name", "bio", "profile_picture")
