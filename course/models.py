from django.utils import timezone
from django.db import models
from category.models import CategoryModel
from user.models import UserModel


class CourseModel(models.Model):
    """Model definition for CourseModel."""
    COURSE_STATUS = (
        ('published', 'published'),
        ('requested', 'requested'),
        ('drafted', 'drafted'),
    )

    course_name = models.TextField()
    created_on = models.DateTimeField(default=timezone.now)
    published_on = models.DateTimeField()
    course_status = models.CharField(choices=COURSE_STATUS,
                                     max_length=14,
                                     default='drafted')
    total_videos = models.IntegerField()
    total_duration = models.IntegerField()
    cover_image = models.URLField(blank=True, null=True)
    cover_image_public_id = models.TextField(blank=True, null=True)
    description = models.TextField(max_length=100)
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


class CourseEnrollmentModel(models.Model):
    """Model definition for CourseEnrollmentModel."""

    student = models.ManyToManyField(UserModel)
    # student = models.ManyToManyField(UserModel, on_delete=models.CASCADE)
    course = models.ManyToManyField(CourseModel)
    # course = models.ManyToManyField(CourseModel, on_delete=models.CASCADE)
    meta_data = models.JSONField(blank=True, null=True)
    created_on = models.DateTimeField(default=timezone.now)

    class Meta:
        """Meta definition for CourseEnrollmentModel."""

        verbose_name = 'Enrollment'
        verbose_name_plural = 'Enrollments'

    def __str__(self):
        """Unicode representation of CourseEnrollmentModel."""
        # return self.student.name
        pass

