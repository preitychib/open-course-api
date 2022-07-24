import logging
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .serializers import CourseVideoSerializer
from .models import CourseVideoModel
from user.permissions import UserIsAdmin, UserIsTeacher

logger = logging.getLogger(__name__)


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
