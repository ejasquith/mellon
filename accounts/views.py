from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from django.views import View
from django.db.models import Q
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse

from .models import CustomUser as User, Friendship
from .forms import CustomUserCreationForm, CustomUserChangeForm


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


class ProfileView(View):
    def get(self, request, slug, *args, **kwargs):
        user = get_object_or_404(User, slug=slug)

        try:
            friendship = Friendship.objects.get(
                Q(sender=request.user, recipient=user) | Q(sender=user, recipient=request.user)
            )
        except ObjectDoesNotExist:
            friendship = None
        return render(
            request,
            "profile.html",
            {
                "user": user,
                "is_current_user": True if user == request.user else False,
                'friendship': friendship
            }
        )


class EditProfileView(UpdateView):
    model = User
    form_class = CustomUserChangeForm
    template_name = 'edit_profile.html'

    def get_success_url(self):
        return reverse_lazy('profile', kwargs={'slug': self.object.slug})


class AddFriendView(View):
    def post(self, request):
        data = request.POST
        recipient = get_object_or_404(User, id=data.get('recipient_id'))
        Friendship.objects.create(
            sender=request.user,
            recipient=recipient,
            status=Friendship.Status.PENDING
        )
        return JsonResponse({
            'status': 'success',
            'msg': {
                'tag': 'alert-success',
                'message': 'Friend request sent.'
            }
        })


class AcceptFriendshipView(View):
    def post(self, request):
        data = request.POST
        sender = User.objects.get(pk=request.POST.get('sender_id'))
        Friendship.objects.filter(recipient=request.user, sender=sender).update(status=Friendship.Status.ACCEPTED)
        return JsonResponse({
            'status': 'success',
            'msg': {
                'tag': 'alert-success',
                'message': 'Friend request accepted.'
            }
        })


class RejectFriendshipView(View):
    def post(self, request):
        data = request.POST
        sender = User.objects.get(pk=request.POST.get('sender_id'))
        Friendship.objects.filter(recipient=request.user, sender=sender).delete()
        return JsonResponse({
            'status': 'success',
            'msg': {
                'tag': 'alert-success',
                'message': 'Friend request rejected.'
            }
        })


class RemoveFriendView(View):
    def post(self, request):
        data = request.POST
        friend = User.objects.get(pk=request.POST.get('user_id'))
        Friendship.objects.filter(
            Q(sender=request.user, recipient=friend) |
            Q(sender=friend, recipient=request.user)
        ).delete()

        return JsonResponse({
            'status': 'success',
            'msg': {
                'tag': 'alert-success',
                'message': 'Friend removed.'
            }
        })


class FriendsListView(View):
    def get(self, request):
        # Get the list of friends for the current user
        friendships = Friendship.objects.filter(
            Q(sender=request.user, status=Friendship.Status.ACCEPTED) |
            Q(recipient=request.user, status=Friendship.Status.ACCEPTED)
        ).values_list('sender', 'recipient')
        # Flatten the list of friends
        friends = [friend[0] for friend in friendships] + [friend[1] for friend in friendships]
        # Exclude the current user from the list of friends
        friends = [friend for friend in friends if friend != request.user.pk]
        # Filter the User objects to include only the current user's friends
        friends = User.objects.filter(pk__in=friends)

        # Get the list of users who have sent friend requests
        pending_requests = Friendship.objects.filter(
            recipient=request.user,
            status=Friendship.Status.PENDING
        ).values_list('sender', flat=True)
        pending_users = User.objects.filter(pk__in=pending_requests)

        return render(
            request,
            'friends_list.html',
            {
                'pending_users': pending_users,
                'friends': friends
            }
        )


class CheckFriendRequestsView(View):
    def post(self, request):
        if request.user.is_authenticated:
            has_requests = Friendship.objects.filter(
                recipient=request.user, status=Friendship.Status.PENDING
            ).exists()
            return JsonResponse({'has_requests': has_requests})
        return JsonResponse({'error': 'User not authenticated'})