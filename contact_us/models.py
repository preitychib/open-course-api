import email
from django.db import models


class ContactUsModel(models.Model):
    """Model definition for ContactUsModel."""

    name = models.TextField()
    email = models.EmailField()
    message = models.TextField(max_length=20)

    class Meta:
        """Meta definition for ContactUsModel."""

        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'

    def __str__(self):
        """Unicode representation of ContactUsModel."""
        pass
