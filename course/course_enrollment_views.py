import logging

from drf_spectacular.utils import OpenApiResponse, extend_schema, extend_schema_view
from drf_spectacular.types import OpenApiTypes

from rest_framework import generics, permissions, status
from rest_framework.response import Response

from rest_framework.filters import OrderingFilter

from .serializers import CourseEnrollmentSerializer, CourseEnrollmentNestedSerializer
from .models import CourseEnrollmentModel
from user.permissions import UserIsAdmin, UserIsTeacher, UserIsStudent
from api.paginator import StandardPagination

logger = logging.getLogger(__name__)


@extend_schema_view(post=extend_schema(
    request=CourseEnrollmentSerializer,
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
    description='Creates a new Course.\n Accessed by: admin and student.'))
class CourseEnrollmentCreateAPIView(generics.CreateAPIView):
    '''
        Allowed methods: POST
        POST: Creates a Category 
        Access: Admin,Student
       
    '''
    queryset = CourseEnrollmentModel.objects.all()
    serializer_class = CourseEnrollmentSerializer
    permission_classes = [
        permissions.IsAuthenticated & (UserIsAdmin | UserIsStudent)
    ]

    # Todo: A alot
    #? Create a new Category
    def post(self, request, *args, **kwargs):
        serializer = CourseEnrollmentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            serializer.save()
        except Exception as ex:
            logger.error(str(ex))

            return Response({'detail': str(ex)},
                            status=status.HTTP_400_BAD_REQUEST)

        response = {'detail': 'Enrolled in Course Successfully'}
        logger.info(response)

        return Response(response, status=status.HTTP_201_CREATED)


@extend_schema_view(get=extend_schema(
    request=CourseEnrollmentNestedSerializer,
    responses={
        #? 200
        status.HTTP_200_OK:
        OpenApiResponse(
            description='Course Enrollment List',
            response=CourseEnrollmentNestedSerializer,
        ),
        #? 400
        status.HTTP_400_BAD_REQUEST:
        OpenApiResponse(
            description='Bad Request',
            response=OpenApiTypes.OBJECT,
        ),
    },
))
class CourseEnrollmentListAPIView(generics.ListAPIView):
    '''
        Allowed methods: GET
        GET: Course List
        Access: Admin,Student
       
    '''

    queryset = CourseEnrollmentModel.objects.all()
    serializer_class = CourseEnrollmentNestedSerializer
    permission_classes = [
        permissions.IsAuthenticated & (UserIsAdmin | UserIsStudent)
    ]
    # Todo: Add another custom permission
    pagination_class = StandardPagination
    filter_backends = [OrderingFilter]
    ordering_fields = 'created_on'
    ordering = '-created_on'
