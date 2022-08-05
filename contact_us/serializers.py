from rest_framework import serializers
from .models import ContactUsModel


class ContactUsSerializer(serializers.Serializer):

    class Meta:
        model = ContactUsModel
        exclude = [
            'created_on',
        ]
