from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from .validators import password_validator, role_validaotr

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
        max_length=30,
        validators=[validate_password, password_validator],
    )
    name = serializers.CharField(min_length=3)

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
        Serializer Valdidator
        """

        if 'is_student' in data and 'is_teacher' in data:

            #? To check if both teacher and student roles are not selected
            if data['is_student'] == True and data['is_teacher'] == True:
                raise serializers.ValidationError(
                    "User can not be  teacher and student at the same time.")

            #? To check if atleast one of the field is selected
            if data['is_student'] == False and data['is_teacher'] == False:
                raise serializers.ValidationError(
                    "You have to select atleat one role")

        return data


class UserCreateAdminSerializer(serializers.ModelSerializer):
    '''
        Serializer for User Creation and Update
    '''

    password = serializers.CharField(
        min_length=8,
        max_length=16,
        validators=[validate_password, password_validator],
    )
    name = serializers.CharField(min_length=3)

    class Meta:
        model = User
        fields = [
            'name',
            'email',
            'bio',
            'is_admin',
            'is_teacher',
            'is_student',
            'password',
        ]

    def validate(self, data):
        """
        Serializer Valdidator
        """

        if 'is_student' in data and 'is_teacher' in data and 'is_admin' in data:
            role_validaotr(data['is_admin'], data['is_teacher'],
                           data['is_student'])

        return data


class UserUpdateAdminSerializer(serializers.ModelSerializer):
    '''
        Serializer for User Updation
    '''
    name = serializers.CharField(min_length=3)

    class Meta:
        model = User
        fields = [
            'name',
            'email',
            'bio',
            'is_admin',
            'is_teacher',
            'is_student',
        ]

    def validate(self, data):
        """
        Serializer Valdidator
        """

        if 'is_student' in data and 'is_teacher' in data and 'is_admin' in data:
            role_validaotr(data['is_admin'], data['is_teacher'],
                           data['is_student'])

        return data


class UserUpdatePasswordAdminSerializer(serializers.Serializer):
    '''
        Serializer for password updation
    '''

    password = serializers.CharField(
        min_length=3,
        max_length=30,
        validators=[validate_password, password_validator],
    )
    confirm_password = serializers.CharField(
        min_length=3,
        max_length=30,
        validators=[validate_password, password_validator],
    )

    def validate(self, data):
        '''
            Check if confirm password and password are same or not
        '''
        if (data['password'] != data['confirm_password']):
            raise serializers.ValidationError("Password doesn't match.")
        return data