from django.contrib import admin
from .models import UserModel


@admin.register(UserModel)
class UserModelAdmin(admin.ModelAdmin):
    '''Admin View for CourseModel'''

    list_display = [
        'name',
        'email',
        'profile_image',
        'bio',
        'created_on',
        'is_admin',
        'is_teacher',
        'is_student',
    ]

    search_fields = [
        'name',
        'email',
    ]
