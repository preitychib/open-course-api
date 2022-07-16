from django.utils import timezone
from django.db import models


class CourseModel(models.Model):
    """Model definition for CourseModel."""
    COURSE_STATUS = (
        ('approved', 'approved'),
        ('not-approved', 'not-approved'),
        ('drafted', 'drafted'),
    )

    course_name = models.TextField()
    created_on = models.DateTimeField(default=timezone.now)

    published_on = models.DateTimeField()
    course_status = models.CharField(choices=COURSE_STATUS, max_length=14)

    # Todo: Add relation fields

    class Meta:
        """Meta definition for CourseModel."""

        verbose_name = 'Course'
        verbose_name_plural = 'Courses'

    def __str__(self):
        """Unicode representation of CourseModel."""
        return self.course_name
