from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('create_post/', views.CreatePost.as_view(), name='create_post'),
    path('create_comment/', views.CreateComment.as_view(), name='create_comment'),
    path('delete_comment/', views.DeleteComment.as_view(), name='delete_comment'),
    path('like_post/', views.LikePost.as_view(), name='like_post'),
]