from django.db import models
from user.models import UserModel
from course.models import CourseModel
from django.utils import timezone


class StudentProgressModel(models.Model):
    """Model definition for StudentProgressModel."""
    course = models.ManyToManyField(CourseModel)
    student = models.ManyToManyField(UserModel)
    # course = models.ForeignKey(CourseModel,
    #                            related_name='course_progress',
    #                            on_delete=models.CASCADE)
    # student = models.ForeignKey(UserModel,
    #                             related_name='student_progress',
    #                             on_delete=models.CASCADE)
    meta_data = models.JSONField(blank=True, null=True)
    created_on = models.DateTimeField(default=timezone.now)

    class Meta:
        """Meta definition for StudentProgressModel."""

        verbose_name = 'StudentProgressModel'
        verbose_name_plural = 'StudentProgressModels'

    def __str__(self):
        """Unicode representation of StudentProgressModel."""
        # return self.student.id
        return self.student
