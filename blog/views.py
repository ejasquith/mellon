from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.db.models import Q
from django.utils import timezone

from .models import Post
from accounts.models import CustomUser as User


class PostList(generic.ListView):
    model = Post
    # Gets the most recent post from each user ordered
    # by user - will be ordered by date in template
    queryset = Post.objects.order_by('author', '-created_on').distinct('author')
    template_name = 'home.html'
