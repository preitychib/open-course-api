from rest_framework import serializers
from .models import StudentProgressModel
from user.models import UserModel
from course.models import CourseModel


class StudentProgressSerializer(serializers.ModelSerializer):
    student = serializers.PrimaryKeyRelatedField(
        queryset=UserModel.objects.filter(is_student=True), many=True)

    course = serializers.PrimaryKeyRelatedField(
        queryset=CourseModel.objects.all(), many=True)

    class Meta:
        model = StudentProgressModel
        exclude = [
            'created_on',
        ]
