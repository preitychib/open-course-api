from rest_framework import serializers
from .models import StudentProgressModel
from user.models import UserModel
from course.models import CourseModel, CourseEnrollmentModel


class StudentProgressPostSerializer(serializers.ModelSerializer):
    student = serializers.PrimaryKeyRelatedField(
        queryset=UserModel.objects.filter(is_student=True), many=True)

    course = serializers.PrimaryKeyRelatedField(
        queryset=CourseModel.objects.all(), many=True)

    class Meta:
        model = StudentProgressModel
        exclude = [
            'created_on',
        ]

    def validate(self, data):

        if not (CourseEnrollmentModel.objects.filter(
                student=data['student'][0],
                course=data['course'][0]).exists()):
            raise serializers.ValidationError(
                'You need to enroll in the course first')

        if StudentProgressModel.objects.filter(
                student=data['student'][0], course=data['course'][0]).exists():
            raise serializers.ValidationError(
                'You can not add multiple progress of same course')

        return data


class StudentProgressSerializer(serializers.ModelSerializer):

    class Meta:
        model = StudentProgressModel
        exclude = [
            'created_on',
            'student',
            'course',
        ]
