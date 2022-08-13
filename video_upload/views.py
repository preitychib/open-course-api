import logging
from urllib import response
import cloudinary.uploader

from drf_spectacular.utils import OpenApiResponse, extend_schema, extend_schema_view
from drf_spectacular.types import OpenApiTypes

from rest_framework import generics, permissions, status
from rest_framework.response import Response

from . import serializers, response_serializers

#? set logger
logger = logging.getLogger(__name__)


@extend_schema_view(
    post=extend_schema(
        request=serializers.VideoUploadSerializer,
        responses={
            #? 201
            status.HTTP_201_CREATED:
            OpenApiResponse(
                description='Video Uploaded Successfully',
                response=response_serializers.VideoUploadResposeSerializer),
            #? 400
            status.HTTP_400_BAD_REQUEST:
            OpenApiResponse(response=OpenApiTypes.OBJECT)
        },
        description=
        'Uploads an Video to cloudinary and returns the url.\n\noptional: Deletes an image if public_id is passed\n\nAccessible by: Authenticated',
    ), )
class VideoUploadAPIView(generics.CreateAPIView):
    '''
        Allowed methods: POST

        Uploads an video to cloudinary and returns the url.

        optional: Deletes an image if public_id is passed.
            
        Accessible by: Authenticated
    '''

    serializer_class = serializers.VideoUploadSerializer
    permission_classes = [permissions.IsAuthenticated]

    #? upload video to Cloudinary and return its url
    def post(self, request, *args, **kwargs):
        print(request.data)
        # if public_id does not exist in request set public_id to ''
        if 'public_id' not in request.data:
            request.data['public_id'] = ''

        instance = self.get_serializer(data=request.data)
        instance.is_valid(raise_exception=True)

        try:
            #? upload video to cloudinary

            uploaded_video = cloudinary.uploader.upload_large(
                instance.validated_data['video'],
                resource_type="video",
                folder=instance.validated_data['folder'],
            )

            #? remove api_key
            uploaded_video.pop('api_key')
            logger.info(uploaded_video)

            #? if public_id is provided delete the video from cloudinary
            if instance.validated_data['public_id']:
                delete_video = cloudinary.uploader.destroy(
                    public_id=instance.validated_data['public_id'], )

                logger.info(delete_video)

        except Exception as ex:
            logger.error(str(ex))

            return Response({'detail': str(ex)},
                            status=status.HTTP_400_BAD_REQUEST)

        response = {
            'video_url': uploaded_video['secure_url'],
            'public_id': uploaded_video['public_id'],
        }
        logger.info(response)

        return Response(response, status=status.HTTP_201_CREATED)
