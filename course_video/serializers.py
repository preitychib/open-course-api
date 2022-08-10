from rest_framework import serializers
from .models import CourseVideoModel


class CourseVideoFullSerializer(serializers.ModelSerializer):
    video_link = serializers.URLField()
    video_link_public_id = serializers.CharField()

    class Meta:
        model = CourseVideoModel
        fields = '__all__'


class CourseVideoSerializer(serializers.ModelSerializer):
    video_link = serializers.URLField()
    video_link_public_id = serializers.CharField()

    class Meta:
        model = CourseVideoModel
        exclude = [
            'created_on',
        ]


class CourseVideoPublicSerializer(serializers.ModelSerializer):

    class Meta:
        model = CourseVideoModel
        exclude = [
            'created_on',
            'video_link',
            'video_link_public_id',
            'duration',
        ]
