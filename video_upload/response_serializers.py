from rest_framework import serializers


class VideoUploadResposeSerializer(serializers.Serializer):
    video_url = serializers.URLField()
    public_id = serializers.CharField()
