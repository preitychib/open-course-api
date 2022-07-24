from xml.dom import ValidationErr
from rest_framework import serializers
from .models import CourseVideoModel


class CourseVideoSerializer(serializers.ModelSerializer):
    video_link = serializers.URLField()
    video_link_public_id = serializers.CharField()

    class Meta:
        model = CourseVideoModel
        exclude = [
            'created_on',
        ]

   