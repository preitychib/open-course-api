from django.db import models
from user.models import UserModel
from django.utils import timezone


class StudentProgressModel(models.Model):
    """Model definition for StudentProgressModel."""

    student = models.ManyToManyField(UserModel)
    meta_data = models.JSONField(blank=True, null=True)
    created_on = models.DateTimeField(default=timezone.now)

    class Meta:
        """Meta definition for StudentProgressModel."""

        verbose_name = 'StudentProgressModel'
        verbose_name_plural = 'StudentProgressModels'

    def __str__(self):
        """Unicode representation of StudentProgressModel."""
        return self.student
