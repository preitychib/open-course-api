from rest_framework import serializers
from course_section.serializers import CourseSectionNestedSerializer
from .models import CourseModel


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
