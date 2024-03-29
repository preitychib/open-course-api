import logging

from drf_spectacular.utils import OpenApiResponse, extend_schema, extend_schema_view
from drf_spectacular.types import OpenApiTypes

from rest_framework import generics, permissions, status
from rest_framework.response import Response

from rest_framework.filters import OrderingFilter

from course_review.models import CourseReviewModel

from .serializers import CourseFullSerializer, CourseGetAllSerializer, CourseNestedFullSerializer, CoursePublicSerializer, CourseSerializer, CourseStatusSerializer, CourseStatusTeacherSerializer, CourseStudentNestedFullSerializer, CourseUpdateSerializer
from django_filters.rest_framework import DjangoFilterBackend

from .models import CourseModel, CourseEnrollmentModel
from user.permissions import UserIsAdmin, UserIsStudent, UserIsTeacher
from api.paginator import StandardPagination

logger = logging.getLogger(__name__)


@extend_schema_view(post=extend_schema(
    request=CourseSerializer,
    responses={
        #? 201
        status.HTTP_201_CREATED:
        OpenApiResponse(description='Course Created Successfully', ),
        #? 400
        status.HTTP_400_BAD_REQUEST:
        OpenApiResponse(
            description='Bad Request',
            response=OpenApiTypes.OBJECT,
        ),
    },
    description='Creates a new Course.\n Accessed by: admin and teacher.'))
class CourseCreateAPIView(generics.CreateAPIView):
    '''
        Allowed methods: POST
        POST: Creates a new Course
        Access: Admin,Teacher
       
    '''
    queryset = CourseModel.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [
        permissions.IsAuthenticated & (UserIsAdmin | UserIsTeacher)
    ]

    #? Create a new Course
    def post(self, request, *args, **kwargs):
        serializer = CourseSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)
        try:
            serializer.save()
        except Exception as ex:
            logger.error(str(ex))

            return Response({'detail': str(ex)},
                            status=status.HTTP_400_BAD_REQUEST)

        response = {'detail': 'Course Created Successfully'}
        logger.info(response)

        return Response(response, status=status.HTTP_201_CREATED)


@extend_schema_view(get=extend_schema(
    request=CourseGetAllSerializer,
    responses={
        #? 200
        status.HTTP_200_OK:
        OpenApiResponse(
            description='Course List',
            response=CourseGetAllSerializer,
        ),
        #? 400
        status.HTTP_400_BAD_REQUEST:
        OpenApiResponse(
            description='Bad Request',
            response=OpenApiTypes.OBJECT,
        ),
    },
))
class CourseListAPIView(generics.ListAPIView):
    '''
        Allowed methods: GET
       GET: Course List
    
       
    '''
    # Todo permissions
    queryset = CourseModel.objects.all()
    serializer_class = CourseGetAllSerializer
    permission_classes = [permissions.IsAuthenticated & (UserIsAdmin)]
    pagination_class = StandardPagination
    filter_backends = [OrderingFilter, DjangoFilterBackend]
    filterset_fields = ['category']
    ordering_fields = 'created_on'
    ordering = '-created_on'


@extend_schema_view(get=extend_schema(
    request=CourseNestedFullSerializer,
    responses={
        #? 200
        status.HTTP_200_OK:
        OpenApiResponse(
            description=
            'Allowed methods: GET\n\nAccess: Teacher,Admin \n\nGET: Course List owned by teacher',
            response=CourseNestedFullSerializer,
        ),
        #? 400
        status.HTTP_400_BAD_REQUEST:
        OpenApiResponse(
            description='Bad Request',
            response=OpenApiTypes.OBJECT,
        ),
    },
))
class CourseListTeacherAPIView(generics.ListAPIView):
    '''
        Allowed methods: GET
        Access: Teacher, Admin
        GET: Course List owned by teacher
        
        
        '''
    serializer_class = CourseNestedFullSerializer
    permission_classes = [
        permissions.IsAuthenticated & (UserIsTeacher or UserIsAdmin)
    ]
    pagination_class = StandardPagination
    filter_backends = [OrderingFilter]
    ordering_fields = 'created_on'
    ordering = '-created_on'

    def get_queryset(self):
        queryset = CourseModel.objects.filter(teacher=self.request.user)
        return queryset


@extend_schema_view(get=extend_schema(
    request=CourseGetAllSerializer,
    responses={
        #? 200
        status.HTTP_200_OK:
        OpenApiResponse(
            description='Course List with status published\n\n Access:Anyone',
            response=CourseGetAllSerializer,
        ),
        #? 400
        status.HTTP_400_BAD_REQUEST:
        OpenApiResponse(
            description='Bad Request',
            response=OpenApiTypes.OBJECT,
        ),
    },
))
class CoursePublishedListAPIView(generics.ListAPIView):
    '''
        Allowed methods: GET
        GET: Course List with status published
        Access: Anyone
    '''
    queryset = CourseModel.objects.all()
    serializer_class = CourseGetAllSerializer
    filter_backends = [OrderingFilter]
    ordering_fields = 'created_on'
    ordering = '-created_on'

    def get(self, request):
        queryset = CourseModel.objects.filter(course_status='published')

        serializer = CourseGetAllSerializer(queryset, many=True)

        return Response({'results': list(serializer.data)})


@extend_schema_view(get=extend_schema(
    request=CourseGetAllSerializer,
    responses={
        #? 200
        status.HTTP_200_OK:
        OpenApiResponse(
            description='Course List with status requested',
            response=CourseGetAllSerializer,
        ),
        #? 400
        status.HTTP_400_BAD_REQUEST:
        OpenApiResponse(
            description='Bad Request',
            response=OpenApiTypes.OBJECT,
        ),
    },
))
class CourseRequestedListAPIView(generics.ListAPIView):
    '''
        Allowed methods: GET
       GET: Course List with status requested
       Access: Admin
    '''
    queryset = CourseModel.objects.filter(course_status='requested')
    serializer_class = CourseGetAllSerializer
    permission_classes = [permissions.IsAuthenticated & (UserIsAdmin)]
    pagination_class = StandardPagination
    ordering_fields = 'created_on'
    ordering = '-created_on'


@extend_schema_view(
    get=extend_schema(
        description=
        'Returns Single Course of given Id.\n\nargs: pk\n\n Access: Everyone\n\nNote: For Admin and Teacher who owns the course the response contains video links\n\n For others the response does not contain video links',
        responses={
            #? 200
            status.HTTP_200_OK:
            OpenApiResponse(
                description='Course Details',
                response=CourseGetAllSerializer,
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
        request=CourseUpdateSerializer,
        responses={
            #? 201
            status.HTTP_201_CREATED:
            OpenApiResponse(description='Course Updated Successfully', ),
            #? 400
            status.HTTP_400_BAD_REQUEST:
            OpenApiResponse(
                description='Bad Request',
                response=OpenApiTypes.OBJECT,
            ),
        },
        description=' Updates a Course \nAccess: Admin, Teacher'))
@extend_schema_view(delete=extend_schema(
    responses={
        #? 201
        status.HTTP_201_CREATED:
        OpenApiResponse(description='Course Deleted Successfully', ),
        #? 400
        status.HTTP_400_BAD_REQUEST:
        OpenApiResponse(
            description='Bad Request',
            response=OpenApiTypes.OBJECT,
        ),
    },
    description='Delete a Course \nAccess: Admin, Teacher'))
class CourseUpdateRetriveDeleteAPIView(generics.GenericAPIView):
    '''
        Allowed methods: Patch
        GET: Course by ID
        PATCH: Update a Course 
        DELETE: Delete a Course 
        Access: Admin, Teacher who owns the course
       
    '''
    queryset = CourseModel.objects.all()
    serializer_class = CourseUpdateSerializer
    # permission_classes = [
    #     permissions.IsAuthenticated & (UserIsAdmin | UserIsTeacher)
    # ]
    lookup_field = 'pk'

    #? get single Course

    def get(self, request, *args, **kwargs):
        course = self.get_object()

        if request.user.is_authenticated and (
                request.user.is_admin or course.teacher.id == request.user.id):

            serializer = CourseNestedFullSerializer(course)

        elif request.user.is_authenticated and CourseEnrollmentModel.objects.filter(
                student=request.user.id, course=course.id).exists():

            if CourseReviewModel.objects.filter(student=request.user.id,
                                                course=course.id).exists():
                course.has_review = True

            serializer = CourseStudentNestedFullSerializer(course)

        elif course.course_status == 'published':

            serializer = CoursePublicSerializer(course)

        else:

            return Response(
                {
                    'detail':
                    'You Do not have the permission to access the course details'
                },
                status=status.HTTP_403_FORBIDDEN)
        return Response(serializer.data)

    #? Update a Course
    def patch(self, request, *args, **kwargs):
        course = self.get_object()
        serializer = CourseSerializer(course, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)

        try:

            if request.user.is_admin or (request.user.is_teacher
                                         and course.course_status == 'drafted'
                                         and course.teacher.id
                                         == request.user.id):

                serializer.save()
            else:
                return Response(
                    {
                        'detail':
                        'You Do not have the permission to Update the course details'
                    },
                    status=status.HTTP_403_FORBIDDEN)

        except Exception as ex:
            logger.error(str(ex))

            return Response({'detail': str(ex)},
                            status=status.HTTP_400_BAD_REQUEST)

        response = {'detail': 'Course Updated Successfully'}
        logger.info(response)

        return Response(response, status=status.HTTP_201_CREATED)

    #? Delete a Course
    def delete(self, request, *args, **kwargs):
        course = self.get_object()
        try:

            if request.user.is_admin or (request.user.is_teacher
                                         and course.course_status == 'drafted'
                                         and course.teacher.id
                                         == request.user.id):

                course.delete()
            else:
                return Response(
                    {
                        'detail':
                        'You Do not have the permission to delete the course'
                    },
                    status=status.HTTP_403_FORBIDDEN)
        except Exception as ex:
            logger.error(str(ex))

            return Response({'detail': str(ex)},
                            status=status.HTTP_400_BAD_REQUEST)

        response = {'detail': 'Course Deleted Successfully'}
        logger.info(response)

        return Response(response, status=status.HTTP_201_CREATED)


@extend_schema_view(patch=extend_schema(
    request=CourseStatusSerializer,
    responses={
        #? 201
        status.HTTP_201_CREATED:
        OpenApiResponse(description='Course Status Updated Successfully', ),
        #? 400
        status.HTTP_400_BAD_REQUEST:
        OpenApiResponse(
            description='Bad Request',
            response=OpenApiTypes.OBJECT,
        ),
    },
    description=
    ' Updates a Course Status \n\n Course Status are: drafted,requested,published \n\n Access: Admin, Teacher\n\nNote:Teacher cannot change course status to published.'
))
class CourseStatusUpdateAPIView(generics.GenericAPIView):
    queryset = CourseModel.objects.all()
    serializer_class = [CourseStatusSerializer, CourseStatusTeacherSerializer]
    permission_classes = [
        permissions.IsAuthenticated & (UserIsAdmin | UserIsTeacher)
    ]

    lookup_field = 'pk'

    #? Update a Course Status
    def patch(self, request, *args, **kwargs):
        course = self.get_object()
        if request.user.is_teacher == True:
            serializer = CourseStatusTeacherSerializer(course,
                                                       data=request.data,
                                                       partial=True)
        else:
            serializer = CourseStatusSerializer(course,
                                                data=request.data,
                                                partial=True)
        serializer.is_valid(raise_exception=True)
        try:
            serializer.save()
        except Exception as ex:
            logger.error(str(ex))

            return Response({'detail': str(ex)},
                            status=status.HTTP_400_BAD_REQUEST)

        response = {'detail': 'Course Status Updated Successfully'}
        logger.info(response)

        return Response(response, status=status.HTTP_201_CREATED)
