import logging

from drf_spectacular.utils import OpenApiResponse, extend_schema, extend_schema_view
from drf_spectacular.types import OpenApiTypes

from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .serializers import StudentProgressSerializer
from .models import StudentProgressModel
from user.permissions import UserIsAdmin, UserIsStudent

logger = logging.getLogger(__name__)


@extend_schema_view(post=extend_schema(
    request=StudentProgressSerializer,
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
    serializer_class = StudentProgressSerializer
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
