import logging

from drf_spectacular.utils import OpenApiResponse, extend_schema, extend_schema_view
from drf_spectacular.types import OpenApiTypes

from rest_framework import generics, permissions, status
from rest_framework.response import Response

from rest_framework.filters import OrderingFilter

from .serializers import CatergorySerializer
from .models import CategoryModel
from user.permissions import UserIsAdmin, UserIsTeacher
from api.paginator import StandardPagination

logger = logging.getLogger(__name__)


@extend_schema_view(post=extend_schema(
    request=CatergorySerializer,
    responses={
        #? 201
        status.HTTP_201_CREATED:
        OpenApiResponse(description='Category Created Successfully', ),
        #? 400
        status.HTTP_400_BAD_REQUEST:
        OpenApiResponse(
            description='Bad Request',
            response=OpenApiTypes.OBJECT,
        ),
    },
    description='Creates a new category.'))
class CategoryCreateAPIView(generics.CreateAPIView):
    '''
        Allowed methods: POST
        POST: Creates a Category 
        Access: Admin
       
    '''
    queryset = CategoryModel.objects.all()
    serializer_class = CatergorySerializer
    permission_classes = [permissions.IsAuthenticated & UserIsAdmin]

    #? Create a new User
    def post(self, request, *args, **kwargs):
        serializer = CatergorySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            serializer.save()
        except Exception as ex:
            logger.error(str(ex))

            return Response({'detail': str(ex)},
                            status=status.HTTP_400_BAD_REQUEST)

        response = {'detail': 'Category Created Successfully'}
        logger.info(response)

        return Response(response, status=status.HTTP_201_CREATED)
