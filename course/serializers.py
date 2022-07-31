from dataclasses import field, fields
from rest_framework import serializers
from course_section.serializers import CourseSectionNestedSerializer
from .models import CourseModel, CourseEnrollmentModel, CourseReviewModel


#? =====================
#? Course Serializers
#? =====================
class CourseFullSerializer(serializers.ModelSerializer):
    '''
        Full Serializer for course
    '''

    class Meta:
        model = CourseModel
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    '''
        Course Serializer
    '''

    class Meta:
        model = CourseModel
        exclude = [
            'created_on',
        ]


class CourseNestedSerializer(serializers.ModelSerializer):
    '''
        Course Serializer to get Nested data 
        Return full data of course 
    '''
    section = CourseSectionNestedSerializer(many=True)

    class Meta:
        model = CourseModel
        fields = '__all__'


class CourseStatusSerializer(serializers.ModelSerializer):
    '''
        Course's status serializer
    '''
    course_status = serializers.CharField(max_length=12)

    class Meta:
        model = CourseModel
        fields = [
            'course_status',
        ]

    # def validated_course_status(self, value):

    #     return value


#? =========================
#? Course Review Serializers
#? =========================


class CourseReviewFullSerializer(serializers.ModelSerializer):
    course = CourseNestedSerializer(many=True)

    class Meta:
        model = CourseReviewModel
        fields = '__all__'


#? =============================
#? Course Enrollment Serializers
#? =============================


class CourseEnrollmentFullSerializer(serializers.ModelSerializer):
    # course = CourseNestedSerializer(many=True)

    class Meta:
        model = CourseEnrollmentModel
        fields = '__all__'
