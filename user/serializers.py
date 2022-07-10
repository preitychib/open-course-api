from urllib.request import DataHandler
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

    def validate_password(self, value):

        #? check if password contain atleast one digit
        if not any(char.isdigit() for char in value):
            raise serializers.ValidationError(
                'Password must contain at least 1 digit.')

        #? check if password contains atleast 1 special character
        if not any(char in '!@#$%^&*()_+' for char in value):
            raise serializers.ValidationError(
                'Password must contain at least one special character')

        #? check if password contains atleast 1 capital letter
        if not any(char.isupper() for char in value):
            raise serializers.ValidationError(
                'Password must contain at least one capital letter')

        #? check if password contains atleast 1 small letter
        if not any(char.islower() for char in value):
            raise serializers.ValidationError(
                "Password must contain at least one small letter")

        return value

    def validate(self, data):
        """
        Serializer Valdidator
        """

        #? To set Name's length 3 character
        if len(data['name']) < 3:
            raise serializers.ValidationError("Name length too short!")

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
        validators=[validate_password],
    )

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

    def validate_password(self, value):

        #? check if password contain atleast one digit
        if not any(char.isdigit() for char in value):
            raise serializers.ValidationError(
                'Password must contain at least 1 digit.')

        #? check if password contains atleast 1 special character
        if not any(char in '!@#$%^&*()_+' for char in value):
            raise serializers.ValidationError(
                'Password must contain at least one special character')

        #? check if password contains atleast 1 capital letter
        if not any(char.isupper() for char in value):
            raise serializers.ValidationError(
                'Password must contain at least one capital letter')

        #? check if password contains atleast 1 small letter
        if not any(char.islower() for char in value):
            raise serializers.ValidationError(
                "Password must contain at least one small letter")

        return value

    def validate(self, data):
        """
        Serializer Valdidator
        """

        #? To set Name's length 3 character
        if len(data['name']) < 3:
            raise serializers.ValidationError("Name length too short!")

        if 'is_student' in data and 'is_teacher' in data and 'is_admin' in data:

            #? To check if both teacher and student roles are not selected
            if (data['is_student'] == True and data['is_teacher'] == True and [
                    'is_admin' == True
            ]) or (data['is_admin'] == True and data['is_teacher']
                   == True) or (data['is_student'] == True and data['is_admin']
                                == True) or (data['is_student'] == True
                                             and data['is_teacher'] == True):
                raise serializers.ValidationError(
                    "User can not have multiple roles")

            #? To check if atleast one of the field is selected
            if data['is_admin'] == False and data[
                    'is_student'] == False and data['is_teacher'] == False:
                raise serializers.ValidationError(
                    "You have to select atleat one role")

        return data


class UserUpdateAdminSerializer(serializers.ModelSerializer):
    '''
        Serializer for User Updation
    '''

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

        #? To set Name's length 3 character
        if 'is_name' in data and len(data['name']) < 3:
            raise serializers.ValidationError("Name length too short!")

        if 'is_student' in data and 'is_teacher' in data and 'is_admin' in data:

            #? To check if both teacher and student roles are not selected
            if (data['is_student'] == True and data['is_teacher'] == True and [
                    'is_admin' == True
            ]) or (data['is_admin'] == True and data['is_teacher']
                   == True) or (data['is_student'] == True and data['is_admin']
                                == True) or (data['is_student'] == True
                                             and data['is_teacher'] == True):
                raise serializers.ValidationError(
                    "User can not have multiple roles")

            #? To check if atleast one of the field is selected
            if data['is_admin'] == False and data[
                    'is_student'] == False and data['is_teacher'] == False:
                raise serializers.ValidationError(
                    "You have to select atleat one role")

        return data
