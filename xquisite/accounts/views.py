from typing import Optional
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import get_user_model
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin 
from django.urls import reverse_lazy
from django.http.response import HttpResponseNotFound
from .forms import SignupForm

User = get_user_model()

class signup(CreateView):
    form_class = SignupForm
    template_name = 'accounts/signup_login.html'
    success_url = reverse_lazy('accounts:login')
    extra_context = {
        'title': 'Signup',
        'action': '/signup/'
    }

class login(LoginView):
    template_name = 'accounts/signup_login.html'
    next_page = reverse_lazy('accounts:profile')
    extra_context = {
        'title': 'Login',
        'action': '/login/'
    }

class logout(LoginRequiredMixin, LogoutView):
    template_name = "accounts/logout.html"
    next_page = reverse_lazy('home')
    extra_context = {
        'title': 'Logout',
        'action': '/logout/',
    }

class Profile(LoginRequiredMixin, DetailView):
    model = User
    template_name = "accounts/profile.html"
    extra_context = {
        'title': 'Profile',
    }
    
    # def get(self, request):
    #     user = get_object_or_404(User, request.user.id)
    #     return render(request, "accounts/profile.html", context={'object': user})
    
    def get_object(self):
        user = get_object_or_404(User, id=self.request.user.id)
        return user

    