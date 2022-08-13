import logging

from drf_spectacular.utils import OpenApiResponse, extend_schema, extend_schema_view
from drf_spectacular.types import OpenApiTypes

from rest_framework import generics, permissions, status
from rest_framework.response import Response

from rest_framework.filters import OrderingFilter

from django_filters.rest_framework import DjangoFilterBackend

from category import serializers
from django.db.models import Count
from .serializers import CourseSectionFullSerializer, CourseSectionNestedSerializer, CourseSectionSerializer
from .models import CourseSectionModel
from user.permissions import UserIsAdmin, UserIsTeacher
from api.paginator import StandardPagination

logger = logging.getLogger(__name__)


@extend_schema_view(post=extend_schema(
    request=CourseSectionSerializer,
    responses={
        #? 201
        status.HTTP_201_CREATED:
        OpenApiResponse(description='Course Section Created Successfully', ),
        #? 400
        status.HTTP_400_BAD_REQUEST:
        OpenApiResponse(
            description='Bad Request',
            response=OpenApiTypes.OBJECT,
        ),
    },
    description=
    'Creates a new Course section.\n Accessed by: admin and teacher.'))
class CourseSectionCreateAPIView(generics.CreateAPIView):
    '''
        Allowed methods: POST
        POST: Creates a Course Section
        Access: Admin,Teacher
       
    '''
    queryset = CourseSectionModel.objects.all()
    serializer_class = CourseSectionSerializer
    permission_classes = [
        permissions.IsAuthenticated & (UserIsAdmin | UserIsTeacher)
    ]

    #? Create a new Category
    def post(self, request, *args, **kwargs):
        serializer = CourseSectionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:

            serializer.save()
        except Exception as ex:
            logger.error(str(ex))

            return Response({'detail': str(ex)},
                            status=status.HTTP_400_BAD_REQUEST)

        response = {'detail': 'Course Section Created Successfully'}
        logger.info(response)

        return Response(response, status=status.HTTP_201_CREATED)


@extend_schema_view(get=extend_schema(
    request=CourseSectionNestedSerializer,
    responses={
        #? 200
        status.HTTP_200_OK:
        OpenApiResponse(
            description='Course Section List',
            response=CourseSectionFullSerializer,
        ),
        #? 400
        status.HTTP_400_BAD_REQUEST:
        OpenApiResponse(
            description='Bad Request',
            response=OpenApiTypes.OBJECT,
        ),
    },
))
class CourseSectionListAPIView(generics.ListAPIView):
    '''
        Allowed methods: GET
       GET: Course Section List
    
       
    '''
    queryset = CourseSectionModel.objects.all()
    serializer_class = CourseSectionNestedSerializer
    pagination_class = StandardPagination
    # Todo permission?
    filter_backends = [OrderingFilter, DjangoFilterBackend]
    filterset_fields = ['course']
    ordering_fields = 'created_on'
    ordering = '-created_on'


@extend_schema_view(patch=extend_schema(
    request=CourseSectionSerializer,
    responses={
        #? 201
        status.HTTP_201_CREATED:
        OpenApiResponse(description='Course Section Updated Successfully', ),
        #? 400
        status.HTTP_400_BAD_REQUEST:
        OpenApiResponse(
            description='Bad Request',
            response=OpenApiTypes.OBJECT,
        ),
    },
    description=' Updates a Course Section\nAccess: Admin, Teacher'))
@extend_schema_view(delete=extend_schema(
    responses={
        #? 201
        status.HTTP_201_CREATED:
        OpenApiResponse(description='Course Section Deleted Successfully', ),
        #? 400
        status.HTTP_400_BAD_REQUEST:
        OpenApiResponse(
            description='Bad Request',
            response=OpenApiTypes.OBJECT,
        ),
    },
    description='Delete a Course Section\nAccess: Admin, Teacher'))
class CourseSectionUpdateDeleteAPIView(generics.GenericAPIView):
    '''
        Allowed methods: Patch
        PATCH: Update a Course Secction
        DELETE: Delete a Course Section
        Access: Admin, Teacher
       
    '''
    queryset = CourseSectionModel.objects.all()
    serializer_class = CourseSectionSerializer
    permission_classes = [
        permissions.IsAuthenticated & (UserIsAdmin | UserIsTeacher)
    ]
    lookup_field = 'pk'

    #? Update a Course Section
    def patch(self, request, *args, **kwargs):
        course_section = self.get_object()
        serializer = CourseSectionSerializer(course_section,
                                             data=request.data,
                                             partial=True)
        serializer.is_valid(raise_exception=True)
        try:
            if request.user.is_admin or (
                    request.user.is_teacher
                    and course_section.course.course_status == 'drafted'
                    and course_section.course.teacher.id == request.user.id):
                serializer.save()
            else:
                return Response(
                    {
                        'detail':
                        'You Do not have the permission to Update the course section details'
                    },
                    status=status.HTTP_403_FORBIDDEN)
        except Exception as ex:
            logger.error(str(ex))

            return Response({'detail': str(ex)},
                            status=status.HTTP_400_BAD_REQUEST)

        response = {'detail': 'Course Section Updated Successfully'}
        logger.info(response)

        return Response(response, status=status.HTTP_201_CREATED)

    #? Delete a course Section
    def delete(self, request, *args, **kwargs):
        course_section = self.get_object()
        try:
            if request.user.is_admin or (
                    request.user.is_teacher
                    and course_section.course.course_status == 'drafted'
                    and course_section.course.teacher.id == request.user.id):
                s = CourseSectionModel.objects.annotate(
                    videos_count=Count('video')).get(id=course_section.id)
                video_count = s.videos_count
                course_section.course.total_videos -= video_count
                course_section.course.save()
                course_section.delete()
            else:
                return Response(
                    {
                        'detail':
                        'You Do not have the permission to delete the course section'
                    },
                    status=status.HTTP_403_FORBIDDEN)
        except Exception as ex:
            logger.error(str(ex))

            return Response({'detail': str(ex)},
                            status=status.HTTP_400_BAD_REQUEST)

        response = {'detail': 'Course Section Deleted Successfully'}
        logger.info(response)

        return Response(response, status=status.HTTP_201_CREATED)
