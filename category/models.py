from django.db import models


class CategoryModel(models.Model):
    """Model definition for CategoryModel."""

    category_name = models.TextField()

    class Meta:
        """Meta definition for CategoryModel."""

        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        """Unicode representation of CategoryModel."""
        return self.category_name
