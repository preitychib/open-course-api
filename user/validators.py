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


def role_validaotr(is_admin, is_teacher, is_student):
    #? To check if both teacher and student roles are not selected
    if (is_student == True and is_teacher == True and is_admin == True) or (
            is_admin == True
            and is_teacher == True) or (is_student == True and is_admin
                                        == True) or (is_student == True
                                                     and is_teacher == True):
        raise serializers.ValidationError("User can not have multiple roles")

    #? To check if atleast one of the field is selected
    if is_admin == False and is_student == False and is_teacher == False:
        raise serializers.ValidationError("You have to select atleat one role")
