from django.shortcuts import render

# Create your views here.
import logging

from drf_spectacular.utils import OpenApiResponse, extend_schema, extend_schema_view
from drf_spectacular.types import OpenApiTypes

from django.contrib.auth import get_user_model

from rest_framework import generics, permissions, status
from rest_framework.response import Response

from .serializers import UserSerializer, UserCreateSerializer
from .permissions import UserIsAdmin

User = get_user_model()
logger = logging.getLogger(__name__)


@extend_schema_view(
    post=extend_schema(
        request=UserCreateSerializer,
        responses={
            #? 201
            status.HTTP_201_CREATED:
            OpenApiResponse(description='User Created Successfully', ),
            #? 400
            status.HTTP_400_BAD_REQUEST:
            OpenApiResponse(
                description='Bad Request',
                response=OpenApiTypes.OBJECT,
            ),
        },
        description='Create a new user with teacher and student roles.'),
    request=UserSerializer,
    responses={
        #? 200
        status.HTTP_200_OK:
        OpenApiResponse(
            description='Users List',
            response=UserSerializer,
        ),
        #? 400
        status.HTTP_400_BAD_REQUEST:
        OpenApiResponse(
            description='Bad Request',
            response=OpenApiTypes.OBJECT,
        ),
    },
)
class UserCreateAPIView(generics.CreateAPIView):
    '''
        Allowed methods: POST
        POST: Creates a new User with teacher and student roles
       
    '''
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer

    #? Create a new User
    def post(self, request, *args, **kwargs):
        serializer = UserCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            User.objects.create_user(
                name=serializer.validated_data['name'],
                email=serializer.validated_data['email'],
                is_teacher=serializer.validated_data['is_teacher'],
                is_student=serializer.validated_data['is_student'],
                password=serializer.validated_data['password'],
            )

        except Exception as ex:
            logger.error(str(ex))

            return Response({'detail': str(ex)},
                            status=status.HTTP_400_BAD_REQUEST)

        response = {'detail': 'User Created Successfully'}
        logger.info(response)

        return Response(response, status=status.HTTP_201_CREATED)