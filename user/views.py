# Create your views here.
import logging

from drf_spectacular.utils import OpenApiResponse, extend_schema, extend_schema_view
from drf_spectacular.types import OpenApiTypes

from django.contrib.auth import get_user_model

from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .permissions import UserIsAdmin

from rest_framework.filters import OrderingFilter

from .serializers import UserSerializer, UserCreateSerializer, UserCreateAdminSerializer, UserUpdateAdminSerializer
from .permissions import UserIsAdmin

from api.paginator import StandardPagination

User = get_user_model()
logger = logging.getLogger(__name__)


@extend_schema_view(post=extend_schema(
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
    description='Create a new user with teacher and student roles.'))
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


@extend_schema_view(
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
    post=extend_schema(
        request=UserCreateAdminSerializer,
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
)
class UserListCreateAdminAPIView(generics.ListCreateAPIView):
    '''
        Allowed methods: GET, POST
        GET: Returns list of all Users
        POST: Creates a new User
        Accessible by: Admin
    '''
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated & (UserIsAdmin)]
    pagination_class = StandardPagination
    filter_backends = [OrderingFilter]
    ordering_fields = 'created_on'
    ordering = '-created_on'

    #? Create a new User
    def post(self, request, *args, **kwargs):
        serializer = UserCreateAdminSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            User.objects.create_user(
                name=serializer.validated_data['name'],
                email=serializer.validated_data['email'],
                password=serializer.validated_data['password'],
                is_admin=serializer.validated_data['is_admin'],
                is_teacher=serializer.validated_data['is_teacher'],
                is_student=serializer.validated_data['is_student'],
                bio=serializer.validated_data['bio'],
            )
        except Exception as ex:
            logger.error(str(ex))

            return Response({'detail': str(ex)},
                            status=status.HTTP_400_BAD_REQUEST)

        response = {'detail': 'User Created Successfully'}
        logger.info(response)

        return Response(response, status=status.HTTP_201_CREATED)


@extend_schema_view(
    get=extend_schema(
        description=
        'Returns Single User registered on Application of given Id.\n\nargs: pk',
        responses={
            #? 200
            status.HTTP_200_OK:
            OpenApiResponse(
                description='User Details',
                response=UserSerializer,
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
        request=UserUpdateAdminSerializer,
        description=
        'Updates the User of given Id with the provided Data.\n\nargs: pk',
        responses={
            #? 200
            status.HTTP_200_OK:
            OpenApiResponse(description='User Updated Successfully', ),
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
    delete=extend_schema(
        description='Deletes the User of the given Id.\n\nargs: pk',
        responses={
            #? 200
            status.HTTP_200_OK:
            OpenApiResponse(description='User Deleted Successfully', ),
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
class UserRetrieveUpdateDestroyAdminAPIView(generics.GenericAPIView):
    '''
        Allowed methods: GET, PATCH, DELETE
        GET: Return User of given Id
        PATCH: Update User of given Id with Validated data provided
        DELETE: Delete User of given Id
        Note: Updatation on User is done via Partial Update method
        args: pk
        
        Accessible by: Admin
    '''
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated & (UserIsAdmin)]
    lookup_field = 'pk'

    #? get single User
    def get(self, request, *args, **kwargs):
        user = self.get_object()
        serializer = UserSerializer(user)
        return Response(serializer.data)

    #? Update User of given Id
    def patch(self, request, *args, **kwargs):
        user = self.get_object()
        serializer = UserUpdateAdminSerializer(user,
                                               data=request.data,
                                               partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        response = {'detail': 'User Updated Successfully'}
        logger.info(response)

        return Response(response, status=status.HTTP_200_OK)

    #? Delete User of given Id
    def delete(self, request, *args, **kwargs):
        user = self.get_object()
        user.delete()

        response = {'detail': 'User Deleted Successfully'}
        logger.info(response)

        return Response(response, status=status.HTTP_200_OK)
