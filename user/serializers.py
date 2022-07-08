from rest_framework import serializers

from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password

from user.models import UserModel

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    '''
        Serializer for User
    '''

    class Meta:
        model = User
        exclude = [
            'is_staff',
            'is_superuser',
            'groups',
            'password',
            'last_login',
            'user_permissions',
        ]


class UserCreateSerializer(serializers.ModelSerializer):
    '''
        Serializer for User Creation/Register with roles except admin
    '''
    password = serializers.CharField(
        min_length=8,
        max_length=16,
        validators=[validate_password],
    )

    class Meta:
        model = User
        fields = [
            'name',
            'email',
            'is_teacher',
            'is_student',
            'password',
        ]

    def validate(self, data):
        """
        Check that if user have one and only one role
        """
        if data['is_student'] == True and data['is_teacher'] == True:
            raise serializers.ValidationError(
                "User can not be  teacher and student at the same time.")
        if data['is_student'] == False and data['is_teacher'] == False:
            raise serializers.ValidationError(
                "You have to select atleat one role")
        return data