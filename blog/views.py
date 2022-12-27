from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.db.models import Q
from django.utils import timezone
from django.http import JsonResponse

from .models import Post, Comment
from accounts.models import CustomUser as User


class PostList(generic.ListView):
    model = Post
    # Gets the most recent post from each user ordered
    # by user - will be ordered by date in template
    queryset = Post.objects.order_by('author', '-created_on').distinct('author')
    template_name = 'home.html'


class CreatePost(View):
    def post(self, request):
        data = request.POST
        body = data.get('body')
        author = request.user
        post = Post.objects.create(body=body, author=author)
        return JsonResponse({'status': 'success'})


class CreateComment(View):
    def post(self, request):
        data = request.POST
        body = data.get('body')
        author = request.user
        post = get_object_or_404(Post, id=data.get('post_id'))
        comment = Comment.objects.create(body=body, author=author, post=post)
        return JsonResponse({
            'status': 'success',
            'author_username': author.username,
            'author_display_name': author.display_name,
            'author_profile_picture_url': author.profile_picture.url,
            'comments_count': comment.post.comments.count()
        })


class LikePost(View):
    def post(self, request):
        data = request.POST
        id = data.get('post_id')
        post = get_object_or_404(Post, id=id)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)
        liked = post.likes.filter(id=request.user.id).exists()

        # Passes back updated data to the template so that
        # relevant fields can be updated easily
        return JsonResponse({
            'status': 'success',
            'num_likes': post.num_likes(),
            'liked': liked
        })
