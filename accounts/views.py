from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views import View
from .models import CustomUser as User
from .forms import CustomUserCreationForm


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


class ProfileView(View):
    def get(self, request, username, *args, **kwargs):
        user = get_object_or_404(User, username=username)
        return render(
            request,
            "profile.html",
            {
                "user": user,
                "is_current_user": True if user == request.user else False
            }
        )