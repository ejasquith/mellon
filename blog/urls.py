from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('create_post/', views.CreatePost.as_view(), name='create_post'),
]