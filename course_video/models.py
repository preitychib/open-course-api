from django.db import models
from course_section.models import CourseSectionModel
from django.utils import timezone


class CourseVideo(models.Model):
    """Model definition for CourseVideo."""

    video_title = models.TextField()
    description = models.TextField()
    video_link = models.URLField(blank=True, null=True)
    video_link_public_id = models.TextField(blank=True, null=True)
    duration = models.IntegerField()
    created_on = models.DateTimeField(default=timezone.now)
    #? Many to one relation with Course Section Model
    section = models.ForeignKey(
        CourseSectionModel,
        on_delete=models.CASCADE,
    )

    class Meta:
        """Meta definition for CourseVideo."""

        verbose_name = 'CourseVideo'
        verbose_name_plural = 'CourseVideos'

    def __str__(self):
        """Unicode representation of CourseVideo."""
        return self.video_title
