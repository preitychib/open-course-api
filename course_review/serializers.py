from rest_framework import serializers
from course.models import CourseModel
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


class CourseReviewNestedSerializer(serializers.ModelSerializer):
    course = CourseSerializer(many=True)
    student = UserSerializer(many=True)

    class Meta:
        model = CourseReviewModel
        fields = '__all__'
