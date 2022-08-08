from unicodedata import category
from rest_framework import serializers
from course_section.serializers import CourseSectionNestedSerializer
from .models import CourseModel, CourseEnrollmentModel
from course_review.models import CourseReviewModel
from user.models import UserModel
from user.serializers import UserSerializer
from category.serializers import CatergorySerializer

#? =====================
#? Course Serializers
#? =====================


class CourseGetAllSerializer(serializers.ModelSerializer):
    '''
        Full Serializer for course
    '''
    teacher = UserSerializer()
    category= CatergorySerializer()
    class Meta:
        model = CourseModel
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    '''
        Course Serializer
    '''

    class Meta:
        model = CourseModel
        exclude = [
            'created_on',
            'total_videos',
            'total_duration',
            'published_on',
            'course_status',
        ]


class CourseUpdateSerializer(serializers.ModelSerializer):
    '''
        Course Serializer
    '''

    class Meta:
        model = CourseModel
        exclude = [
            'created_on',
            'course_status',
        ]


class CourseReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = CourseReviewModel
        exclude = [
            'created_on',
        ]


class CourseNestedFullSerializer(serializers.ModelSerializer):
    '''
        Course Serializer to get Nested data 
        Return full data of course 
    '''
    teacher = UserSerializer()
    section = CourseSectionNestedSerializer(many=True)
    review = CourseReviewSerializer(many=True)

    class Meta:
        model = CourseModel
        fields = '__all__'
        depth = 1


class CourseStatusSerializer(serializers.ModelSerializer):
    '''
        Course's status serializer
    '''
    course_status = serializers.ChoiceField((
        ('drafted', 'drafted'),
        ('requested', 'requested'),
        ('published', 'published'),
    ))

    class Meta:
        model = CourseModel
        fields = [
            'course_status',
        ]


class CourseStatusTeacherSerializer(serializers.ModelSerializer):
    '''
        Course's status serializer for Teacher
    '''
    course_status = serializers.ChoiceField((
        ('drafted', 'drafted'),
        ('requested', 'requested'),
    ))

    class Meta:
        model = CourseModel
        fields = [
            'course_status',
        ]


#? =============================
#? Course Enrollment Serializers
#? =============================


class CourseEnrollmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = CourseEnrollmentModel
        exclude = [
            'created_on',
            'meta_data',
        ]


class CourseEnrollmentNestedSerializer(serializers.ModelSerializer):
    course = CourseNestedFullSerializer(many=True)
    student = UserSerializer(many=True)

    class Meta:
        model = CourseEnrollmentModel
        fields = '__all__'
