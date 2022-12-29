from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.db.models import Q
from django.utils import timezone
from django.http import JsonResponse
from django.template import RequestContext

from .models import Post, Comment
from accounts.models import CustomUser as User, Friendship


class PostList(generic.ListView):
    model = Post
    template_name = 'home.html'
    
    def get_queryset(self):
        if self.request.user.is_authenticated:
            # Gets the most recent post from each user ordered
            # by user - will be ordered by date in template
            queryset = Post.objects.order_by('author', '-created_on').distinct('author')
            # Gets list of friendships for current user
            active_friendships = Friendship.objects.filter(
                Q(sender=self.request.user, status=Friendship.Status.ACCEPTED) |
                Q(recipient=self.request.user, status=Friendship.Status.ACCEPTED)
            ).values_list('sender', 'recipient')
            # Flattens list
            friends = [friend[0] for friend in active_friendships] + [friend[1] for friend in active_friendships]
            # Exclude current user
            friends = [friend for friend in friends if friend != self.request.user.pk]
            # Filter queryset to only include friends
            return queryset.filter(author__in=friends)


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


class DeletePost(View):
    def post(self, request):
        data = request.POST
        id = data.get('post_id')
        post = get_object_or_404(Post, id=id)
        if request.user == post.author:
            post.delete()
            return JsonResponse({
                'status': 'success',                
                'msg': {
                    'tag': 'alert-success',
                    'message': 'Post deleted'
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


def handler404(request, *args, **argv):
    response = render(
        request,
        '404.html',
        {},
    )
    response.status_code = 404
    return response


def handler500(request, *ars, **argv):
    response = render(
        request,
        '500.html',
        {},
    )
    response.status_code = 500
    return response