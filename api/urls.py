from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
#? drf-spectacular
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView, SpectacularJSONAPIView

from user import views as UserViews

from image_upload import views as ImageUploadViews

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
         UserViews.UserRetrieveUpdateAdminAPIView.as_view(),
         name='user-retrieve-update'),
    path('users/delete/<int:pk>/',
         UserViews.UserDestroyAdminAPIView.as_view(),
         name='user-delete-admin'),
    path('users/current-user/',
         UserViews.UserRetrieveUpdateAPIView.as_view(),
         name='user-retrieve-update'),
    #? Image Upload
    path('image-upload/',
         ImageUploadViews.ImageUploadAPIView.as_view(),
         name='image-upload'),
]
