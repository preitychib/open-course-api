import imp
import logging

from drf_spectacular.utils import OpenApiResponse, extend_schema, extend_schema_view
from drf_spectacular.types import OpenApiTypes
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .serializers import CourseVideoFullSerializer, CourseVideoSerializer
from .models import CourseVideoModel
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
            description='Categories List',
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
       GET: Category List
    
       
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
        POST: Creates a new Video
        Access:Admin And Teacher 
    '''

    queryset = CourseVideoModel.objects.all()
    serializer_class = CourseVideoSerializer
    permission_classes = [
        permissions.IsAuthenticated & (UserIsAdmin | UserIsTeacher)
    ]

    #? Creates a new Video
    def post(self, request, *args, **kwargs):
        serializer = CourseVideoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            serializer.save()

        except Exception as ex:
            logger.error(str(ex))

            return Response({'detail': str(ex)},
                            status=status.HTTP_400_BAD_REQUEST)

        response = {'detail': 'Video Created Successfully'}
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

    #? Update a Category
    def patch(self, request, *args, **kwargs):
        category = self.get_object()
        serializer = CourseVideoSerializer(category,
                                           data=request.data,
                                           partial=True)
        serializer.is_valid(raise_exception=True)
        try:
            serializer.save()
        except Exception as ex:
            logger.error(str(ex))

            return Response({'detail': str(ex)},
                            status=status.HTTP_400_BAD_REQUEST)

        response = {'detail': 'Course Video Updated Successfully'}
        logger.info(response)

        return Response(response, status=status.HTTP_201_CREATED)

    #? Delete a Category
    def delete(self, request, *args, **kwargs):
        category = self.get_object()
        try:
            category.delete()
        except Exception as ex:
            logger.error(str(ex))

            return Response({'detail': str(ex)},
                            status=status.HTTP_400_BAD_REQUEST)

        response = {'detail': 'Course video Deleted Successfully'}
        logger.info(response)

        return Response(response, status=status.HTTP_201_CREATED)
