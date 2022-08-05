import logging

from drf_spectacular.utils import OpenApiResponse, extend_schema, extend_schema_view
from drf_spectacular.types import OpenApiTypes

from rest_framework import generics, permissions, status
from rest_framework.response import Response

from rest_framework.filters import OrderingFilter

from .serializers import ContactUsSerializer
from .models import ContactUsModel
from user.permissions import UserIsAdmin
from api.paginator import StandardPagination

logger = logging.getLogger(__name__)


@extend_schema_view(post=extend_schema(
    request=ContactUsSerializer,
    responses={
        #? 201
        status.HTTP_201_CREATED:
        OpenApiResponse(
            description='Contact Us Message Created Successfully', ),
        #? 400
        status.HTTP_400_BAD_REQUEST:
        OpenApiResponse(
            description='Bad Request',
            response=OpenApiTypes.OBJECT,
        ),
    },
    description='Creates a contact us message\n Accessed by:anyone'))
class ContactUsCreateAPIView(generics.CreateAPIView):
    '''
        Allowed methods: POST
        POST: Creates a contact us message
        Access: anyone
       
    '''
    queryset = ContactUsModel.objects.all()
    serializer_class = ContactUsSerializer

    #? Create a new Contact Us Message
    def post(self, request, *args, **kwargs):
        serializer = ContactUsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            serializer.save()
        except Exception as ex:
            logger.error(str(ex))

            return Response({'detail': str(ex)},
                            status=status.HTTP_400_BAD_REQUEST)

        response = {'detail': 'Contact Us Message Created Successfully'}
        logger.info(response)

        return Response(response, status=status.HTTP_201_CREATED)


@extend_schema_view(get=extend_schema(
    request=ContactUsSerializer,
    responses={
        #? 200
        status.HTTP_200_OK:
        OpenApiResponse(
            description='Contact Us List',
            response=ContactUsSerializer,
        ),
        #? 400
        status.HTTP_400_BAD_REQUEST:
        OpenApiResponse(
            description='Bad Request',
            response=OpenApiTypes.OBJECT,
        ),
    },
))
class ContactUsAdminListAPIView(generics.ListAPIView):
    '''
        Allowed methods: GET
        GET: Contact Us List
        Access: Admin
       
    '''

    queryset = ContactUsModel.objects.all()
    serializer_class = ContactUsSerializer
    permission_classes = [permissions.IsAuthenticated & (UserIsAdmin)]
    pagination_class = StandardPagination
    filter_backends = [OrderingFilter]
    ordering_fields = 'created_on'
    ordering = '-created_on'
