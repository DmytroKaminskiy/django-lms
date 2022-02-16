from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
# Create your views here.
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from accounts.forms import AccountRegisterForm, AccountProfileForm


class AccountRegister(CreateView):
    model = User
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('index')
    form_class = AccountRegisterForm


class AccountLogin(LoginView):
    template_name = 'accounts/login.html'

    def form_valid(self, form):
        result = super().form_valid(form)

        messages.success(
            self.request,
            f'User {self.request.user.username} logged in successfully'
        )

        return result


class AccountEdit(LoginRequiredMixin, UpdateView):
    model = User
    template_name = 'accounts/profile.html'
    success_url = reverse_lazy('accounts:profile')
    form_class = AccountProfileForm

    def get_object(self, queryset=None):
        return self.request.user

    def form_valid(self, form):
        result = super().form_valid(form)

        messages.success(
            self.request,
            f'Profile updated successfully'
        )

        return result
