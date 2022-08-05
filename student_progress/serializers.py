from rest_framework import serializers
from .models import StudentProgressModel


class StudentProgressSerializer(serializers.ModelSerializer):

    class Meta:
        model = StudentProgressModel
        exclude = [
            'created_on',
        ]
