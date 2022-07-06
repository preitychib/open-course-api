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
        Serializer for User Creation
    '''
    password = serializers.CharField(
        min_length=8,
        max_length=16,
        validators=[validate_password],
    )
    confirm_password = serializers.CharField(
        min_length=8,
        max_length=16,
        validators=[validate_password],
    )

    class Meta:
        model = User
        fields = [
            'profile_image',
            'name',
            'email',
            'bio',
            'is_admin',
            'is_teacher',
            'is_student',
            'password',
            'confirm_password',
        ]

    def validate(self, attrs):
        if attrs['password'] != attrs['confirm_password']:
            raise serializers.ValidationError(
                {'error': 'Confirm Password does not match Password'})

        return attrs