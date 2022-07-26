from django.db import models
from course.models import CourseModel
from django.utils import timezone


class CourseSectionModel(models.Model):
    """Model definition for CourseSectionModel."""
    section_tittle = models.TextField()
    description = models.TextField()
    created_on = models.DateTimeField(default=timezone.now)

    #? Many to one realtion with couse model
    course = models.ForeignKey(
        CourseModel,
        on_delete=models.CASCADE,
        related_name='section',
    )

    # TODO: max and min length

    class Meta:
        """Meta definition for CourseSectionModel."""

        verbose_name = 'Section'
        verbose_name_plural = 'Sections'

    def __str__(self):
        """Unicode representation of CourseSectionModel."""
        return self.section_tittle
