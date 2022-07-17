from django.utils import timezone
from django.db import models
from category.models import CategoryModel
from user.models import UserModel


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
    total_videos = models.IntegerField()
    total_duration = models.IntegerField()
    #? Many to one realtion with Category Model
    category = models.ForeignKey(
        CategoryModel,
        on_delete=models.SET_NULL,
        null=True,
    )
    #? Many to one relation with User Model
    teacher = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )

    class Meta:
        """Meta definition for CourseModel."""

        verbose_name = 'Course'
        verbose_name_plural = 'Courses'

    def __str__(self):
        """Unicode representation of CourseModel."""
        return self.course_name
