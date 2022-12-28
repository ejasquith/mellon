from django.urls import path
from .views import *

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('user/<slug:slug>', ProfileView.as_view(), name='profile'),
    path('user/<slug:slug>/edit', EditProfileView.as_view(), name='edit_profile'),
    path('add_friend', AddFriendView.as_view(), name='add_friend'),
    path('friends', FriendsListView.as_view(), name='friends_list'),
    path('accept_friend_request', AcceptFriendshipView.as_view(), name='accept_friend_request')
]
