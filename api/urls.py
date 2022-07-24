import imp
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
#? drf-spectacular
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView, SpectacularJSONAPIView

from user import views as UserViews

from image_upload import views as ImageUploadViews

from video_upload import views as VideoUploadViews

from category import views as CategoryViews

from course import views as CourseViews

from course_video import views as CourseVideoViews

from course_section import views as CourseSectionViews

urlpatterns = [

    #? Schema
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('schema/json/', SpectacularJSONAPIView.as_view(), name='json_schema'),
    path('schema/swagger/',
         SpectacularSwaggerView.as_view(url_name='schema'),
         name='swagger'),
    path('schema/redoc/',
         SpectacularRedocView.as_view(url_name='schema'),
         name='redoc'),

    # ? Authentication Token
    path('auth/signin',
         TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('auth/signup',
         UserViews.UserCreateAPIView.as_view(),
         name='user-sign-up'),

    #? User
    path('users/',
         UserViews.UserListCreateAdminAPIView.as_view(),
         name='user-create-list-admin'),
    path('users/<int:pk>/',
         UserViews.UserRetrieveUpdateDestroyAdminAPIView.as_view(),
         name='user-retrieve-update-destroy'),

    #? Image Upload
    path('image-upload/',
         ImageUploadViews.ImageUploadAPIView.as_view(),
         name='image-upload'),

    #? Video Upload
    path('video-upload/',
         VideoUploadViews.VideoUploadAPIView.as_view(),
         name='video-upload'),

    #? Category
    path('category/',
         CategoryViews.CategoryCreateAPIView.as_view(),
         name='category-create'),
    path('category/<int:pk>/',
         CategoryViews.CategoryUpdateDeleteAPIView.as_view(),
         name='category-update-delete'),
    path('category/all/',
         CategoryViews.CategoryListAPIView.as_view(),
         name='category-list'),

    #? Course
    path('course/',
         CourseViews.CourseCreateAPIView.as_view(),
         name='course-create'),
    path('course/<int:pk>/',
         CourseViews.CourseUpdateDeleteAPIView.as_view(),
         name='course-update-delete'),
    path('course/all/',
         CourseViews.CourseListAPIView.as_view(),
         name='course-list'),

    #? Course Section
    path('course-section/',
         CourseSectionViews.CourseSectionCreateAPIView.as_view(),
         name='course-section-create'),
    path('course-section/<int:pk>/',
         CourseSectionViews.CourseSectionUpdateDeleteAPIView.as_view(),
         name='course-section-update-delete'),
    path('course-section/all/',
         CourseSectionViews.CourseSectionListAPIView.as_view(),
         name='course-section-list'),

    #? Course Video
    path('course-video/',
         CourseVideoViews.CourseVideoCreateAPIView.as_view(),
         name='course-video-create'),
    path('course-video/all/',
         CourseVideoViews.CourseVideoListAPIView.as_view(),
         name='course-video-list'),
    path('course-video/<int:pk>/',
         CourseVideoViews.CourseVideoUpdateDeleteAPIView.as_view(),
         name='course-video-update-delete'),
]
