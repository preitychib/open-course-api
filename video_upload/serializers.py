from rest_framework import serializers
#? max size 10 mb
MAX_UPLOAD_SIZE = 104857600


class VideoUploadSerializer(serializers.Serializer):
    '''
        Serializer to Upload Video and delete when needed
    '''
    video = serializers.FileField(required=True)
    folder = serializers.CharField(required=True)
    public_id = serializers.CharField(allow_blank=True)

    def validate_video(self, value):
        '''
            Validations for video
            Validates if its Empty
            Validates if its a valid image
            Validates if its of a valid size
        '''
        
        if not value:
            raise serializers.ValidationError('No video provided.')

        #? check image format
        if value.content_type not in [
                'video/mp4',
                'video/mov',
                'video/webm',
                'video/mkv',
        ]:
            raise serializers.ValidationError(
                'Video must be MP4 or WEBM or MOV or MKV.')

        #? check image size
        if value.size > MAX_UPLOAD_SIZE:
            raise serializers.ValidationError(
                'Video size must be less than 10 MB.')

        return value

    def validate_folder(self, value):
        '''
            Validations for folder
            
            Validates if folder is empty
        '''
        if not value:
            raise serializers.ValidationError('No folder provided.')

        return value

    def validate_public_id(self, value):
        '''
            Validations for public_id
            
            Validates if public_id is string if not blank
        '''
        if value and not isinstance(value, str):
            raise serializers.ValidationError('public_id must be a string.')

        return value
