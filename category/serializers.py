from rest_framework import serializers
from .models import CategoryModel


class CatergorySerializer(serializers.ModelSerializer):

    class Meta:
        model = CategoryModel
        fields = '__all__'

    # Todo: Validation
    def validate(self, attrs):
        return super().validate(attrs)
