from django.db import models


class CourseVideo(models.Model):
    """Model definition for CourseVideo."""

    video_title = models.TextField()
    #description=models.TextField()
    # section= 1:n
    video_link = models.URLField(blank=True, null=True)
    video_link_public_id = models.TextField(blank=True, null=True)

    # TODO: Define fields here

    class Meta:
        """Meta definition for CourseVideo."""

        verbose_name = 'CourseVideo'
        verbose_name_plural = 'CourseVideos'

    def __str__(self):
        """Unicode representation of CourseVideo."""
        pass
