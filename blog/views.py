from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.contrib import messages
from .models import Post

class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.all().order_by('-created_on')
    template_name = 'home.html'