from rest_framework import serializers
from .models import Book


class BookSerializer(serializers.ModelSerializer):
    image = serializers.FileField(write_only=True)

    class Meta:
        model = Book
        fields = '__all__'
        read_only_fields = ['image_url']
