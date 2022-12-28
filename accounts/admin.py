from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserChangeForm
from .models import CustomUser, Friendship


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    form = CustomUserChangeForm

    fieldsets = (
        (None, {
            'fields': ('username', 'password', 'email', 'display_name', 'bio', 'profile_picture')
        }),
    )
    model = CustomUser
    list_display = ["username", "email",]


@admin.register(Friendship)
class FriendshipAdmin(admin.ModelAdmin):
    list_display = ('sender', 'recipient', 'status')
