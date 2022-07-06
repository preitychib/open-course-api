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
        description='Create a new user.'),
    get=extend_schema(
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
        description='Returns list of all Users.'),
)
class UserListCreateAPIView(generics.ListCreateAPIView):
    '''
        Allowed methods: GET, POST
        GET: Returns list of all Users
        POST: Creates a new User
        Accessible by: Admin
    '''
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated & (UserIsAdmin)]

    #? Create a new User
    def post(self, request, *args, **kwargs):
        serializer = UserCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            User.objects.get_or_create(
                profile_image=serializer.validated_data['profile_image'],
                name=serializer.validated_data['name'],
                email=serializer.validated_data['email'],
                bio=serializer.validated_data['bio'],
                is_admin=serializer.validated_data['is_admin'],
                is_teacher=serializer.validated_data['is_teacher'],
                is_student=serializer.validated_data['is_student'],
            )

        except Exception as ex:
            logger.error(str(ex))

            return Response({'detail': str(ex)},
                            status=status.HTTP_400_BAD_REQUEST)

        response = {'detail': 'User Created Successfully'}
        logger.info(response)

        return Response(response, status=status.HTTP_201_CREATED)
