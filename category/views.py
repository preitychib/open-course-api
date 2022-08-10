import logging

from drf_spectacular.utils import OpenApiResponse, extend_schema, extend_schema_view
from drf_spectacular.types import OpenApiTypes

from rest_framework import generics, permissions, status
from rest_framework.response import Response

from rest_framework.filters import OrderingFilter

from .serializers import CatergoryFullSerializer, CatergorySerializer
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

    #? Create a new Category
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


@extend_schema_view(get=extend_schema(
    request=CatergoryFullSerializer,
    responses={
        #? 200
        status.HTTP_200_OK:
        OpenApiResponse(
            description='Categories List',
            response=CatergoryFullSerializer,
        ),
        #? 400
        status.HTTP_400_BAD_REQUEST:
        OpenApiResponse(
            description='Bad Request',
            response=OpenApiTypes.OBJECT,
        ),
    },
))
class CategoryListAPIView(generics.ListAPIView):
    '''
        Allowed methods: GET
       GET: Category List
    
       
    '''
    queryset = CategoryModel.objects.all()
    serializer_class = CatergoryFullSerializer

    # pagination_class = StandardPagination
    # filter_backends = [OrderingFilter]
    # ordering_fields = 'created_on'
    # ordering = '-created_on'

    def get(self, request):
        queryset = CategoryModel.objects.all().values()
        return Response({'results': list(queryset)})


@extend_schema_view(patch=extend_schema(
    request=CatergorySerializer,
    responses={
        #? 201
        status.HTTP_201_CREATED:
        OpenApiResponse(description='Category Updated Successfully', ),
        #? 400
        status.HTTP_400_BAD_REQUEST:
        OpenApiResponse(
            description='Bad Request',
            response=OpenApiTypes.OBJECT,
        ),
    },
    description='Updates a new category.'))
@extend_schema_view(delete=extend_schema(
    responses={
        #? 201
        status.HTTP_201_CREATED:
        OpenApiResponse(description='Category Deleted Successfully', ),
        #? 400
        status.HTTP_400_BAD_REQUEST:
        OpenApiResponse(
            description='Bad Request',
            response=OpenApiTypes.OBJECT,
        ),
    },
    description='Delete a new category.'))
class CategoryUpdateDeleteAPIView(generics.GenericAPIView):
    '''
        Allowed methods: Patch
        POST: Creates a Category 
        Access: Admin
       
    '''
    queryset = CategoryModel.objects.all()
    serializer_class = CatergorySerializer
    permission_classes = [permissions.IsAuthenticated & UserIsAdmin]
    lookup_field = 'pk'

    #? Update a Category
    def patch(self, request, *args, **kwargs):
        category = self.get_object()
        serializer = CatergorySerializer(category,
                                         data=request.data,
                                         partial=True)
        serializer.is_valid(raise_exception=True)
        try:
            serializer.save()
        except Exception as ex:
            logger.error(str(ex))

            return Response({'detail': str(ex)},
                            status=status.HTTP_400_BAD_REQUEST)

        response = {'detail': 'Category Updated Successfully'}
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

        response = {'detail': 'Category Deleted Successfully'}
        logger.info(response)

        return Response(response, status=status.HTTP_201_CREATED)
