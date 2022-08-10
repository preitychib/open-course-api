import logging

from drf_spectacular.utils import OpenApiResponse, extend_schema, extend_schema_view
from drf_spectacular.types import OpenApiTypes

from rest_framework import generics, permissions, status
from rest_framework.response import Response

from rest_framework.filters import OrderingFilter

from django_filters.rest_framework import DjangoFilterBackend

from .serializers import CourseEnrollmentPostSerializer, CourseEnrollmentStudentSerializer, CourseEnrollmentTeacherSerializer
from .models import CourseEnrollmentModel
from user.permissions import UserIsAdmin, UserIsTeacher, UserIsStudent
from api.paginator import StandardPagination

logger = logging.getLogger(__name__)


@extend_schema_view(post=extend_schema(
    request=CourseEnrollmentPostSerializer,
    responses={
        #? 201
        status.HTTP_201_CREATED:
        OpenApiResponse(description='Enrolled in Course Successfully', ),
        #? 400
        status.HTTP_400_BAD_REQUEST:
        OpenApiResponse(
            description='Bad Request',
            response=OpenApiTypes.OBJECT,
        ),
    },
    description='Enroll Student in a Course.\n Accessed by: admin and student.'
))
class CourseEnrollmentCreateAPIView(generics.CreateAPIView):
    '''
        Allowed methods: POST
        POST: Enroll Student in a Course
        Access: Admin,Student
       
    '''
    queryset = CourseEnrollmentModel.objects.all()
    serializer_class = CourseEnrollmentPostSerializer
    permission_classes = [
        permissions.IsAuthenticated & (UserIsAdmin | UserIsStudent)
    ]

    # Todo: A alot
    #? Create a new Course Enrollment
    def post(self, request, *args, **kwargs):
        serializer = CourseEnrollmentPostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            if CourseEnrollmentModel.objects.filter(
                    student=request.data['student'][0],
                    course=request.data['course'][0]).exists():

                return Response(
                    {'detail': 'Student have already enrolled in this course'},
                    status=status.HTTP_400_BAD_REQUEST)

            serializer.save()
        except Exception as ex:
            logger.error(str(ex))

            return Response({'detail': str(ex)},
                            status=status.HTTP_400_BAD_REQUEST)

        response = {'detail': 'Enrolled in Course Successfully'}
        logger.info(response)

        return Response(response, status=status.HTTP_201_CREATED)


@extend_schema_view(get=extend_schema(
    request=CourseEnrollmentStudentSerializer,
    responses={
        #? 200
        status.HTTP_200_OK:
        OpenApiResponse(
            description='Course Enrollment List of Current Student',
            response=CourseEnrollmentStudentSerializer,
        ),
        #? 400
        status.HTTP_400_BAD_REQUEST:
        OpenApiResponse(
            description='Bad Request',
            response=OpenApiTypes.OBJECT,
        ),
    },
))
class CourseStudentEnrollmentsListAPIView(generics.ListAPIView):
    '''
        Allowed methods: GET
        GET: Course List
        Access: Admin,Student
       
    '''
    serializer_class = CourseEnrollmentStudentSerializer
    permission_classes = [
        permissions.IsAuthenticated & (UserIsAdmin | UserIsStudent)
    ]
    pagination_class = StandardPagination
    filter_backends = [OrderingFilter]
    ordering_fields = 'created_on'
    ordering = '-created_on'
    filter_backends = [OrderingFilter]

    def get_queryset(self):
        queryset = CourseEnrollmentModel.objects.filter(
            student=self.request.user)
        return queryset


@extend_schema_view(get=extend_schema(
    request=CourseEnrollmentTeacherSerializer,
    responses={
        #? 200
        status.HTTP_200_OK:
        OpenApiResponse(
            description='Course Enrollment List of Current Student',
            response=CourseEnrollmentTeacherSerializer,
        ),
        #? 400
        status.HTTP_400_BAD_REQUEST:
        OpenApiResponse(
            description='Bad Request',
            response=OpenApiTypes.OBJECT,
        ),
    },
))
class CourseTeacherEnrollmentsListAPIView(generics.ListAPIView):
    '''
        Allowed methods: GET
        GET: Course List
        Access: Admin,Teacher
       
    '''
    serializer_class = CourseEnrollmentTeacherSerializer
    permission_classes = [
        permissions.IsAuthenticated & (UserIsAdmin | UserIsTeacher)
    ]
    pagination_class = StandardPagination
    filter_backends = [OrderingFilter]
    ordering_fields = 'created_on'
    ordering = '-created_on'
    filter_backends = [OrderingFilter]

    def get_queryset(self):
        queryset = CourseEnrollmentModel.objects.filter(
            course=self.kwargs['course'])
        return queryset