from rest_framework import serializers
from course_section.serializers import CourseSectionNestedPublicSerializer, CourseSectionNestedSerializer
from .models import CourseModel, CourseEnrollmentModel
from course_review.models import CourseReviewModel
from user.models import UserModel
from user.serializers import UserSerializer
from category.serializers import CatergorySerializer

#? =====================
#? Course Serializers
#? =====================


class CourseFullSerializer(serializers.ModelSerializer):

    class Meta:
        model = CourseModel
        fields = '__all__'


class CoursePublicSerializer(serializers.ModelSerializer):
    teacher = UserSerializer()
    category = CatergorySerializer()
    section = CourseSectionNestedPublicSerializer(many=True)

    class Meta:
        model = CourseModel
        fields = '__all__'


class CourseGetAllSerializer(serializers.ModelSerializer):
    '''
        Full Serializer for course list
    '''
    teacher = UserSerializer()
    category = CatergorySerializer()

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


class ReviewSerializer(serializers.ModelSerializer):

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
    review = ReviewSerializer(many=True)

    class Meta:
        model = CourseModel
        fields = '__all__'
        depth = 1


class CourseStudentNestedFullSerializer(serializers.ModelSerializer):
    '''
        Course Serializer to get Nested data 
        Return full data of course for enrolled students
    '''
    teacher = UserSerializer()
    section = CourseSectionNestedSerializer(many=True)
    has_review = serializers.BooleanField(default=False)

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


class CourseEnrollmentPostSerializer(serializers.ModelSerializer):

    class Meta:
        model = CourseEnrollmentModel
        exclude = [
            'created_on',
            'meta_data',
        ]


class CourseEnrollmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = CourseEnrollmentModel
        exclude = [
            'created_on',
        ]


class CourseEnrollmentStudentUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = CourseEnrollmentModel
        fields = [
            'meta_data',
        ]


class CourseEnrollmentStudentSerializer(serializers.ModelSerializer):
    course = CourseFullSerializer(many=True)

    class Meta:
        model = CourseEnrollmentModel
        fields = '__all__'


class CourseEnrollmentTeacherSerializer(serializers.ModelSerializer):
    student = UserSerializer(many=True)

    class Meta:
        model = CourseEnrollmentModel
        fields = '__all__'
