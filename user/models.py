from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils import timezone


class UserModel(AbstractBaseUser, PermissionsMixin):
    """Model definition for UserModel."""
    username = None
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    profile_image = models.URLField(blank=True)
    created_on = models.DateTimeField(default=timezone.now)
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        """Meta definition for UserModel."""

        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        """Unicode representation of UserModel."""
        return self.name
