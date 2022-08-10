from django.utils import timezone
from django.db import models
from course.models import CourseModel
from user.models import UserModel


class CourseReviewModel(models.Model):
    """Model definition for CourseReviewModel."""

    student = models.ManyToManyField(UserModel)
    course = models.ManyToManyField(CourseModel, related_name='review')
    rating = models.IntegerField()
    feedback = models.TextField(blank=True, null=True)
    created_on = models.DateTimeField(default=timezone.now)

    class Meta:
        """Meta definition for CourseReviewModel."""

        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'

    def __str__(self):
        """Unicode representation of CourseReviewModel."""
        return str(self.rating)
