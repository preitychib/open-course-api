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

from course import course_enrollment_views as CourseEnrollViews

from course_review import views as CourseReviewViews

from course_video import views as CourseVideoViews

from course_section import views as CourseSectionViews

from student_progress import views as StudProgressViews

from contact_us import views as ContactUsViews

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
    path('users/current-user',
         UserViews.CurrentUserRetrieveUpdateAPIView.as_view(),
         name='user-current-retrieve-update'),
    path('users/<int:pk>/',
         UserViews.UserRetrieveUpdateDestroyAdminAPIView.as_view(),
         name='user-retrieve-update-destroy'),
    path('users/update-password/<int:pk>',
         UserViews.UserPasswordUpdateAdminAPIView.as_view(),
         name='user-password-update-admin'),

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
         CourseViews.CourseUpdateRetriveDeleteAPIView.as_view(),
         name='course-retrive-update-delete'),
    path('course/all/',
         CourseViews.CourseListAPIView.as_view(),
         name='course-list'),
    path('course/all-teacher',
         CourseViews.CourseListTeacherAPIView.as_view(),
         name='course-list'),
    path('course/all-requested/',
         CourseViews.CourseRequestedListAPIView.as_view(),
         name='course-requested-list'),
    path('course/change-status/<int:pk>/',
         CourseViews.CourseStatusUpdateAPIView.as_view(),
         name='course-change-status'),

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

    #? Course Enrollemt
    path('course-enroll/',
         CourseEnrollViews.CourseEnrollmentCreateAPIView.as_view(),
         name='course-enroll-create'),
    path('course-enroll/all/',
         CourseEnrollViews.CourseEnrollmentListAPIView.as_view(),
         name='course-enroll-list'),

    #? Course Review
    path('course-review/',
         CourseReviewViews.CourseReviewCreateAPIView.as_view(),
         name='course-review-create'),
    path('course-review/all/',
         CourseReviewViews.CourseReviewListAPIView.as_view(),
         name='course-review-list'),
    path('course-review/<int:pk>/',
         CourseReviewViews.CourseReviewUpdateRetriveDeleteAPIView.as_view(),
         name='course-review-update-delete-retrive'),

    #? Contact Us
    path('contact-us/',
         ContactUsViews.ContactUsCreateAPIView.as_view(),
         name='contact-us-create'),
    path('contact-us/all/',
         ContactUsViews.ContactUsAdminListAPIView.as_view(),
         name='contact-us-list'),
    path('contact-us/<int:pk>/',
         ContactUsViews.ContactUsAdminUpdateDeleteAPIView.as_view(),
         name='contact-us-update-delete'),

    #? Student Progress
    path('student-progress/',
         StudProgressViews.StudentProgressCreateAPIView.as_view(),
         name='student-progress-create'),
    path('student-progress/<int:pk>/',
         StudProgressViews.StudentProgressRetrieveUpdateAPIView.as_view(),
         name='student-progress-retrive-update'),
]
