from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import ModelForm

from accounts.models import Profile


class AccountRegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = ("username", 'first_name', 'last_name', 'email')


class UserEditForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        fields = ('first_name', 'last_name', 'email')


class ProfileEditForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
