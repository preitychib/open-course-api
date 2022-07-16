from django.db import models


class CourseSectionModel(models.Model):
    """Model definition for CourseSectionModel."""
    section_tittle = models.TextField()
    
    # description = models.TextField() / json?
    # course=models 1:n

    # TODO: Define realion fields here

    class Meta:
        """Meta definition for CourseSectionModel."""

        verbose_name = 'Section'
        verbose_name_plural = 'Sections'

    def __str__(self):
        """Unicode representation of CourseSectionModel."""
        return self.section_tittle
