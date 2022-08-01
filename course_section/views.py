import logging

from drf_spectacular.utils import OpenApiResponse, extend_schema, extend_schema_view
from drf_spectacular.types import OpenApiTypes

from rest_framework import generics, permissions, status
from rest_framework.response import Response

from rest_framework.filters import OrderingFilter

from .serializers import CourseSectionFullSerializer, CourseSectionSerializer
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
    request=CourseSectionFullSerializer,
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
    serializer_class = CourseSectionFullSerializer
    pagination_class = StandardPagination
    filter_backends = [OrderingFilter]
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

    #? Update a Category
    def patch(self, request, *args, **kwargs):
        category = self.get_object()
        serializer = CourseSectionSerializer(category,
                                             data=request.data,
                                             partial=True)
        serializer.is_valid(raise_exception=True)
        try:
            serializer.save()
        except Exception as ex:
            logger.error(str(ex))

            return Response({'detail': str(ex)},
                            status=status.HTTP_400_BAD_REQUEST)

        response = {'detail': 'Course Section Updated Successfully'}
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

        response = {'detail': 'Course Section Deleted Successfully'}
        logger.info(response)

        return Response(response, status=status.HTTP_201_CREATED)
