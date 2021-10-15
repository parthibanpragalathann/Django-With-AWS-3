from rest_framework import serializers
from .models import book_box


class book_box_serializer(serializers.ModelSerializer):
    class Meta:
        model = book_box
        fields = '__all__'