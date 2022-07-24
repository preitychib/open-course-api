from rest_framework import serializers
from .models import CourseSectionModel


class CourseSectionFullSerializer(serializers.ModelSerializer):
    video_link = serializers.URLField()
    video_link_public_id = serializers.CharField()

    class Meta:
        model = CourseSectionModel
        fields = '__all__'


class CourseSectionSerializer(serializers.ModelSerializer):
    video_link = serializers.URLField()
    video_link_public_id = serializers.CharField()

    class Meta:
        model = CourseSectionModel
        exclude = [
            'created_on',
        ]
