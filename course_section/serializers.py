from rest_framework import serializers
from .models import CourseSectionModel


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
