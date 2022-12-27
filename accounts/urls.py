from django.urls import path
from .views import SignUpView, ProfileView, EditProfileView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('user/<slug:slug>', ProfileView.as_view(), name='profile'),
    path('user/<slug:slug>/edit', EditProfileView.as_view(), name='edit_profile')
]
