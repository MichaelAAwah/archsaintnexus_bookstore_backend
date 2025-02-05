from rest_framework import serializers
from .models import Blog


class BlogSerializer(serializers.ModelSerializer):
    image = serializers.FileField(write_only=True)

    class Meta:
        model = Blog
        fields = '__all__'
        read_only_fields = ['image_url']
