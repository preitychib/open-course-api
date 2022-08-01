import logging

from drf_spectacular.utils import OpenApiResponse, extend_schema, extend_schema_view
from drf_spectacular.types import OpenApiTypes

from rest_framework import generics, permissions, status
from rest_framework.response import Response

from rest_framework.filters import OrderingFilter

from .serializers import CourseReviewSerializer, CourseReviewNestedSerializer
from .models import CourseReviewModel
from user.permissions import UserIsAdmin, UserIsStudent
from api.paginator import StandardPagination

logger = logging.getLogger(__name__)


@extend_schema_view(post=extend_schema(
    request=CourseReviewSerializer,
    responses={
        #? 201
        status.HTTP_201_CREATED:
        OpenApiResponse(description='Course Review Created Successfully', ),
        #? 400
        status.HTTP_400_BAD_REQUEST:
        OpenApiResponse(
            description='Bad Request',
            response=OpenApiTypes.OBJECT,
        ),
    },
    description='Creates Course Review.\n Accessed by: admin and student.'))
class CourseReviewCreateAPIView(generics.CreateAPIView):
    '''
        Allowed methods: POST
        POST:Creates Course Review.
        Access: Admin,Student
       
    '''
    queryset = CourseReviewModel.objects.all()
    serializer_class = CourseReviewSerializer
    permission_classes = [
        permissions.IsAuthenticated & (UserIsAdmin | UserIsStudent)
    ]

    # Todo: A alot
    #? Create a new Course Review
    def post(self, request, *args, **kwargs):
        serializer = CourseReviewSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            serializer.save()
        except Exception as ex:
            logger.error(str(ex))

            return Response({'detail': str(ex)},
                            status=status.HTTP_400_BAD_REQUEST)

        response = {'detail': 'Course Review Created Successfully'}
        logger.info(response)

        return Response(response, status=status.HTTP_201_CREATED)


@extend_schema_view(get=extend_schema(
    request=CourseReviewNestedSerializer,
    responses={
        #? 200
        status.HTTP_200_OK:
        OpenApiResponse(
            description='Course Review List',
            response=CourseReviewNestedSerializer,
        ),
        #? 400
        status.HTTP_400_BAD_REQUEST:
        OpenApiResponse(
            description='Bad Request',
            response=OpenApiTypes.OBJECT,
        ),
    },
))
class CourseReviewListAPIView(generics.ListAPIView):
    '''
        Allowed methods: GET
        GET: Course List
        Access: Admin,Student
       
    '''

    queryset = CourseReviewModel.objects.all()
    serializer_class = CourseReviewNestedSerializer
    permission_classes = [
        permissions.IsAuthenticated & (UserIsAdmin | UserIsStudent)
    ]
    # Todo: Add another custom permission
    pagination_class = StandardPagination
    filter_backends = [OrderingFilter]
    ordering_fields = 'created_on'
    ordering = '-created_on'
