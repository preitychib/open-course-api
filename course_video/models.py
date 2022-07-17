from tkinter import CASCADE
from django.db import models
from category.models import CategoryModel
from course_section.models import CourseSectionModel


class CourseVideo(models.Model):
    """Model definition for CourseVideo."""

    video_title = models.TextField()
    description = models.TextField()
    #? Many to one relation with Course Section Model
    section = models.ForeignKey(CourseSectionModel, on_delete=models.CASCADE)
    video_link = models.URLField(blank=True, null=True)
    video_link_public_id = models.TextField(blank=True, null=True)

    # TODO: Duration field?

    class Meta:
        """Meta definition for CourseVideo."""

        verbose_name = 'CourseVideo'
        verbose_name_plural = 'CourseVideos'

    def __str__(self):
        """Unicode representation of CourseVideo."""
        return self.video_title
