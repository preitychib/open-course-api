from rest_framework import serializers


def password_validator(value):

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

