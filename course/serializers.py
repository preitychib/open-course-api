from dataclasses import fields
from rest_framework import serializers
from .models import CourseModel


class CourseFullSerializer(serializers.ModelSerializer):
    '''
        full Serializer for course
    '''

    class Meta:
        model = CourseModel
        fields = '__all__'
        depth = 2


class CourseSerializer(serializers.ModelSerializer):
    '''
            course Serializer
    '''

    class Meta:
        model = CourseModel
        exclude = {
            'created_on',
        }
        depth = 2


class CourseAdminSerializer(serializers.ModelSerializer):
    '''
            course Serializer
    '''

    class Meta:
        model = CourseModel
        exclude = {
            'created_on',
        }
        depth = 2
