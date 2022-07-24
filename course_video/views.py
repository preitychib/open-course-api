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
