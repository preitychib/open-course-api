import logging

from drf_spectacular.utils import OpenApiResponse, extend_schema, extend_schema_view
from drf_spectacular.types import OpenApiTypes

from rest_framework import generics, permissions, status
from rest_framework.response import Response

from django_filters.rest_framework import DjangoFilterBackend

from django.http import Http404

from .serializers import StudentProgressSerializer, StudentProgressPostSerializer
from .models import StudentProgressModel
from user.permissions import UserIsAdmin, UserIsStudent

logger = logging.getLogger(__name__)


@extend_schema_view(post=extend_schema(
    request=StudentProgressPostSerializer,
    responses={
        #? 201
        status.HTTP_201_CREATED:
        OpenApiResponse(description='Student Progress Added Successfully', ),
        #? 400
        status.HTTP_400_BAD_REQUEST:
        OpenApiResponse(
            description='Bad Request',
            response=OpenApiTypes.OBJECT,
        ),
    },
    description='Adds Student Progress\n Accessed by:Student'))
class StudentProgressCreateAPIView(generics.CreateAPIView):
    '''
        Allowed methods: POST
        POST: Creates a contact us message
        Access: Student
       
    '''
    queryset = StudentProgressModel.objects.all()
    serializer_class = StudentProgressPostSerializer
    permission_classes = [permissions.IsAuthenticated & (UserIsStudent)]

    #? Adds Student Progress
    def post(self, request, *args, **kwargs):
        serializer = StudentProgressSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            serializer.save()
        except Exception as ex:
            logger.error(str(ex))

            return Response({'detail': str(ex)},
                            status=status.HTTP_400_BAD_REQUEST)

        response = {'detail': 'Student Progress Added Successfully'}
        logger.info(response)

        return Response(response, status=status.HTTP_201_CREATED)


@extend_schema_view(
    get=extend_schema(
        description=
        'Return Progress of Course of Current Student\n\nargs: Course pk',
        responses={
            #? 200
            status.HTTP_200_OK:
            OpenApiResponse(
                description=
                'Return Progress of Course of Current Student\n\nargs: Course pk',
                response=StudentProgressSerializer,
            ),
            #? 404
            status.HTTP_404_NOT_FOUND:
            OpenApiResponse(
                description='Not found',
                response=OpenApiTypes.OBJECT,
            ),
            #? 400
            status.HTTP_400_BAD_REQUEST:
            OpenApiResponse(
                description='Bad Request',
                response=OpenApiTypes.OBJECT,
            ),
        }),
    patch=extend_schema(
        request=StudentProgressSerializer,
        description=
        'Updates the Student Progress of Current Student in a given Course.\n\nargs: pk',
        responses={
            #? 200
            status.HTTP_200_OK:
            OpenApiResponse(
                description='Student Progress Updated Successfully', ),
            #? 404
            status.HTTP_404_NOT_FOUND:
            OpenApiResponse(
                description='Not found',
                response=OpenApiTypes.OBJECT,
            ),
            #? 400
            status.HTTP_400_BAD_REQUEST:
            OpenApiResponse(
                description='Bad Request',
                response=OpenApiTypes.OBJECT,
            ),
        }),
)
class StudentProgressUpdateAPIView(generics.GenericAPIView):
    '''
        Allowed methods: PATCH
        GET: Return Progress of  Student
        PATCH: Updates the Student Progress of  Student.
        Note: Updatation on Student Progress is done via Partial Update method
        
        Accessible by: Student
    '''

    queryset = StudentProgressModel.objects.all()
    serializer_class = StudentProgressSerializer
    permission_classes = [permissions.IsAuthenticated & UserIsStudent]
    lookup_field = 'pk'

    def get_object(self):
        try:
            return StudentProgressModel.objects.get(
                student=self.request.user.id, course=self.kwargs['course'])
        except StudentProgressModel.DoesNotExist:
            raise Http404

    #? get student progess
    def get(self, request, *args, **kwargs):
        progress = self.get_object()
        serializer = StudentProgressSerializer(progress)
        return Response(serializer.data)

    #? Update Student Progress of given Id
    def patch(self, request, *args, **kwargs):

        progress = self.get_object()
        serializer = StudentProgressSerializer(progress,
                                               data=request.data,
                                               partial=True)
        serializer.is_valid(raise_exception=True)
        try:
            serializer.save()
        except Exception as ex:
            logger.error(str(ex))

            return Response({'detail': str(ex)},
                            status=status.HTTP_400_BAD_REQUEST)

        response = {'detail': 'Student Progress Updated Successfully'}
        logger.info(response)

        return Response(response, status=status.HTTP_201_CREATED)
