from django.db import models
from course_section.models import CourseSectionModel
from django.utils import timezone


class CourseVideoModel(models.Model):
    """Model definition for CourseVideoModel."""

    video_title = models.TextField()
    description = models.TextField()
    video_link = models.URLField(null=True)
    video_link_public_id = models.TextField(blank=True, null=True)
    duration = models.IntegerField(null=True)
    created_on = models.DateTimeField(default=timezone.now)
    #? Many to one relation with Course Section Model
    section = models.ForeignKey(
        CourseSectionModel,
        on_delete=models.CASCADE,
        related_name='video',
    )

    class Meta:
        """Meta definition for CourseVideoModel."""

        verbose_name = 'Video'
        verbose_name_plural = 'Videos'

    def __str__(self):
        """Unicode representation of CourseVideoModel."""
        return self.video_title
