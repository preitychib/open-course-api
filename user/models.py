from django.db import models
from django.contrib.auth.models import AbstractBaseUser

class UserModel(models.Model):
    """Model definition for UserModel."""

    # TODO: Define fields here

    class Meta:
        """Meta definition for UserModel."""

        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        """Unicode representation of UserModel."""
        pass
