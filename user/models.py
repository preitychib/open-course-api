from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils import timezone
from .managers import UserManager


class UserModel(AbstractBaseUser, PermissionsMixin):
    """Model definition for UserModel."""
    username = None
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    profile_image = models.URLField(blank=True, null=True)
    profile_image_public_id = models.TextField(blank=True, null=True)
    bio = models.TextField(blank=True)
    created_on = models.DateTimeField(default=timezone.now)
    history = models.JSONField(null=True)
    is_admin = models.BooleanField(
        default=False,
        help_text='Is the Person Admin or not.',
    )
    is_staff = models.BooleanField(
        default=False,
        help_text=('Designates whether user can log into the API Admin Site.'))

    is_teacher = models.BooleanField(
        default=False,
        help_text=('Is the Person Teacher or not.'),
    )
    is_student = models.BooleanField(
        default=False,
        help_text='Is the Person Student or not',
    )
    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        """Meta definition for UserModel."""

        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        """Unicode representation of UserModel."""
        return self.name
