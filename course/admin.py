from django.contrib import admin
from .models import CourseModel, CourseEnrollmentModel

admin.site.register(CourseModel)
# admin.site.register(CourseReviewModel)
admin.site.register(CourseEnrollmentModel)