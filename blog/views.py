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
        return JsonResponse({
            'status': 'success',
            # Hacky way to display messages with ajax requests
            # Doesn't actually use messages framework
            'msg': {
                'tag': 'alert-success',
                'message': 'Post created successfully.'
            }
        })


class CreateComment(View):
    def post(self, request):
        data = request.POST
        body = data.get('body')
        author = request.user
        post = get_object_or_404(Post, id=data.get('post_id'))
        comment = Comment.objects.create(body=body, author=author, post=post)
        return JsonResponse({
            'status': 'success',
            'author': {
                'username': author.username,
                'display_name': author.display_name,
                'profile_picture_url': author.profile_picture.url
            },
            'comments_count': comment.post.comments.count(),
            'msg': {
                'tag': 'alert-success',
                'message': 'Comment created successfully'
            }
        })


class DeleteComment(View):
    def post(self, request):
        data = request.POST
        id = data.get('comment_id')
        comment = get_object_or_404(Comment, id=id)
        if request.user == comment.author:
            comment.delete()
            return JsonResponse({
                'status': 'success',
                'post_id': comment.post.id,
                'comments_count': comment.post.comments.count(),
                
                'msg': {
                    'tag': 'alert-success',
                    'message': 'Comment deleted'
                }
            })
        else:
            return JsonResponse({
                'status': 'error',
                'msg': {
                    'tag': 'alert-error',
                    'message': 'An error occurred. Please try again.'
                }
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

        return JsonResponse({
            'status': 'success',
            'num_likes': post.num_likes(),
            'liked': liked
        })
