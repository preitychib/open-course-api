from rest_framework import serializers
from course.models import CourseModel, CourseEnrollmentModel
from .models import CourseReviewModel
from user.models import UserModel
from user.serializers import UserSerializer
from course.serializers import CourseSerializer

#? =========================
#? Course Review Serializers
#? =========================


class CourseReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = CourseReviewModel
        exclude = [
            'created_on',
        ]


class CourseReviewPostSerializer(serializers.ModelSerializer):

    class Meta:
        model = CourseReviewModel
        exclude = [
            'created_on',
        ]

    def validate(self, data):

        if not (CourseEnrollmentModel.objects.filter(
                student=data['student'][0],
                course=data['course'][0]).exists()):
            raise serializers.ValidationError(
                'You need to enroll in the course first')

        if CourseReviewModel.objects.filter(student=data['student'][0],
                                            course=data['course'][0]).exists():
            raise serializers.ValidationError(
                'You can not add multiple review of same course')

        return data


class CourseReviewNestedSerializer(serializers.ModelSerializer):
    course = CourseSerializer(many=True)
    student = UserSerializer(many=True)

    class Meta:
        model = CourseReviewModel
        fields = '__all__'
