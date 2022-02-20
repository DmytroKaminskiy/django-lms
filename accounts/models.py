from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
from django.db import models


# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(
        to='auth.User',
        on_delete=models.CASCADE,
        related_name="profile"
    )
    image = models.ImageField(
        null=True,
        upload_to='pics/',
        blank=True,
        validators=[
            FileExtensionValidator(['jpg', 'png'])
        ]
    )

    @classmethod
    def generate_profiles(cls):
        for user in User.objects.all():
            try:
                user.profile
            except:
                profile = Profile()
                profile.user = user
                profile.save()
