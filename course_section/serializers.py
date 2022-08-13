from rest_framework import serializers
from .models import CourseSectionModel
from course_video.serializers import CourseVideoFullSerializer, CourseVideoPublicSerializer


class CourseSectionFullSerializer(serializers.ModelSerializer):

    class Meta:
        model = CourseSectionModel
        fields = '__all__'


class CourseSectionSerializer(serializers.ModelSerializer):

    class Meta:
        model = CourseSectionModel
        exclude = [
            'created_on',
        ]


class CourseSectionNestedSerializer(serializers.ModelSerializer):
    video = CourseVideoFullSerializer(many=True)

    class Meta:
        model = CourseSectionModel
        fields = '__all__'


class CourseSectionNestedPublicSerializer(serializers.ModelSerializer):
    video = CourseVideoPublicSerializer(many=True)

    class Meta:
        model = CourseSectionModel
        fields = '__all__'
