from django.db import models
from django.utils import timezone


class CategoryModel(models.Model):
    """Model definition for CategoryModel."""

    category_name = models.TextField()
    created_on = models.DateTimeField(default=timezone.now)

    class Meta:
        """Meta definition for CategoryModel."""

        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        """Unicode representation of CategoryModel."""
        return self.category_name
