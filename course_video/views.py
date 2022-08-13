import logging

from drf_spectacular.utils import OpenApiResponse, extend_schema, extend_schema_view
from drf_spectacular.types import OpenApiTypes
from rest_framework import generics, permissions, status
from rest_framework.response import Response

from .serializers import CourseVideoFullSerializer, CourseVideoSerializer
from .models import CourseVideoModel
from course.models import CourseModel
from user.permissions import UserIsAdmin, UserIsTeacher

from rest_framework.filters import OrderingFilter
from api.paginator import StandardPagination

logger = logging.getLogger(__name__)


@extend_schema_view(get=extend_schema(
    request=CourseVideoFullSerializer,
    responses={
        #? 200
        status.HTTP_200_OK:
        OpenApiResponse(
            description='List of all Course Videos',
            response=CourseVideoFullSerializer,
        ),
        #? 400
        status.HTTP_400_BAD_REQUEST:
        OpenApiResponse(
            description='Bad Request',
            response=OpenApiTypes.OBJECT,
        ),
    },
))
class CourseVideoListAPIView(generics.ListAPIView):
    '''
       Allowed methods: GET
       GET:Course Video List
       Access:Authenticated
    
       
    '''
    queryset = CourseVideoModel.objects.all()
    serializer_class = CourseVideoFullSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = StandardPagination
    filter_backends = [OrderingFilter]
    ordering_fields = 'created_on'
    ordering = '-created_on'


class CourseVideoCreateAPIView(generics.CreateAPIView):
    '''
        Allowed methods: POST
        POST: Creates a new Course Video
        Access:Admin And Teacher 
    '''

    queryset = CourseVideoModel.objects.all()
    serializer_class = CourseVideoSerializer
    permission_classes = [
        permissions.IsAuthenticated & (UserIsAdmin | UserIsTeacher)
    ]

    #? Creates a new Course Video
    def post(self, request, *args, **kwargs):
        serializer = CourseVideoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            course = CourseModel.objects.filter(
                section=request.data['section']).first()
            course.total_videos += 1
            course.save()
            serializer.save()
        except Exception as ex:
            logger.error(str(ex))

            return Response({'detail': str(ex)},
                            status=status.HTTP_400_BAD_REQUEST)

        response = {'detail': 'Course Video Created Successfully'}
        logger.info(response)

        return Response(response, status=status.HTTP_201_CREATED)


@extend_schema_view(patch=extend_schema(
    request=CourseVideoSerializer,
    responses={
        #? 201
        status.HTTP_201_CREATED:
        OpenApiResponse(description='Course Video Updated Successfully', ),
        #? 400
        status.HTTP_400_BAD_REQUEST:
        OpenApiResponse(
            description='Bad Request',
            response=OpenApiTypes.OBJECT,
        ),
    },
    description=' Updates a Course Video\nAccess: Admin, Teacher'))
@extend_schema_view(delete=extend_schema(
    responses={
        #? 201
        status.HTTP_201_CREATED:
        OpenApiResponse(description='Course video Deleted Successfully', ),
        #? 400
        status.HTTP_400_BAD_REQUEST:
        OpenApiResponse(
            description='Bad Request',
            response=OpenApiTypes.OBJECT,
        ),
    },
    description='Delete a Course Video\nAccess: Admin, Teacher'))
class CourseVideoUpdateDeleteAPIView(generics.GenericAPIView):
    '''
        Allowed methods: Patch
        PATCH: Update a Course Video
        DELETE: Delete a Course video
        Access: Admin, Teacher
       
    '''
    queryset = CourseVideoModel.objects.all()
    serializer_class = CourseVideoSerializer
    permission_classes = [
        permissions.IsAuthenticated & (UserIsAdmin | UserIsTeacher)
    ]
    lookup_field = 'pk'

    #? Update a Course Video
    def patch(self, request, *args, **kwargs):
        course_video = self.get_object()
        serializer = CourseVideoSerializer(course_video,
                                           data=request.data,
                                           partial=True)
        serializer.is_valid(raise_exception=True)

        try:

            if request.user.is_admin or (
                    request.user.is_teacher and
                    course_video.section.course.course_status == 'drafted' and
                    course_video.section.course.teacher.id == request.user.id):
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

        response = {'detail': 'Course Video Updated Successfully'}
        logger.info(response)

        return Response(response, status=status.HTTP_201_CREATED)

    #? Delete a Course Video
    def delete(self, request, *args, **kwargs):
        course_video = self.get_object()
        try:
            if request.user.is_admin or (
                    request.user.is_teacher and
                    course_video.section.course.course_status == 'drafted' and
                    course_video.section.course.teacher.id == request.user.id):

                course_video.section.course.total_videos -= 1
                course_video.section.course.save()
                course_video.delete()
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

        response = {'detail': 'Course video Deleted Successfully'}
        logger.info(response)

        return Response(response, status=status.HTTP_201_CREATED)
