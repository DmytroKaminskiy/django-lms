from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import ModelForm
from django.core.mail import send_mail
from django.conf import settings

from accounts.models import Profile
from accounts.tasks import send_registration_email


class AccountRegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = ("username", 'first_name', 'last_name', 'email')

    def save(self, *args, **kwargs):
        self._send_email()
        return super().save(*args, **kwargs)

    def _send_email(self):
        send_registration_email.delay(self.cleaned_data['email'])


class UserEditForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        fields = ('first_name', 'last_name', 'email')


class ProfileEditForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
