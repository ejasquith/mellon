from django.urls import path
from .views import *

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('user/<slug:slug>', ProfileView.as_view(), name='profile'),
    path('user/<slug:slug>/edit', EditProfileView.as_view(), name='edit_profile'),
    path('add_friend', AddFriendView.as_view(), name='add_friend'),
    path('friends', FriendsListView.as_view(), name='friends_list'),
    path('accept_friend_request', AcceptFriendshipView.as_view(), name='accept_friend_request'),
    path('reject_friend_request', RejectFriendshipView.as_view(), name='reject_friend_request'),
    path('cancel_friend_request', CancelFriendshipView.as_view(), name='cancel_friend_request'),
    path('remove_friend', RemoveFriendView.as_view(), name='remove_friend'),
    path('check_friend_requests', CheckFriendRequestsView.as_view(), name='check_friend_requests'),
    path('find_friends', FindFriendsView.as_view(), name='find_friends')
]
