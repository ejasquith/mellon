from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from django.views import View
from django.db.models import Q
from .models import CustomUser as User, Friendship
from .forms import CustomUserCreationForm, CustomUserChangeForm


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


class ProfileView(View):
    def get(self, request, slug, *args, **kwargs):
        user = get_object_or_404(User, slug=slug)

        has_friendship = Friendship.objects.filter(
            Q(sender=request.user, recipient=user) | Q(sender=user, recipient=request.user)
        ).exists()

        return render(
            request,
            "profile.html",
            {
                "user": user,
                "is_current_user": True if user == request.user else False,
                "has_friendship": has_friendship
            }
        )


class EditProfileView(UpdateView):
    model = User
    form_class = CustomUserChangeForm
    template_name = 'edit_profile.html'

    def get_success_url(self):
        return reverse_lazy('profile', kwargs={'slug': self.object.slug})
