from rest_framework import serializers
from .models import CategoryModel


class CatergorySerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(
        min_length=3,
        max_length=50,
    )

    class Meta:
        model = CategoryModel
        exclude = [
            'created_on',
        ]
