from django.shortcuts import render
from rest_framework import generics, filters
from .models import Blog
from .serializers import BlogSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
import cloudinary.uploader
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class BlogListView(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'author']
    ordering_fields = ['title']


class BlogDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'author']
    ordering_fields = ['title', 'author', 'pub_date']


# Endpoints for creating, updating, deleting, and viewings

# Blogs
class BlogCreateView(generics.CreateAPIView):
    # queryset = Blog.objects.all()
    # serializer_class = BlogSerializer
    # permission_classes = [IsAuthenticatedOrReadOnly]

    def post(self, request):
        serializer = BlogSerializer(data=request.data)
        if serializer.is_valid():
            title = serializer.validated_data['title']
            author = serializer.validated_data['author']
            content = serializer.validated_data['content']
            image = serializer.validated_data['image']

            # Upload to Cloudinary
            upload_result = cloudinary.uploader.upload(image)

            if 'secure_url' in upload_result:
                image_url = upload_result['secure_url']
                
                # Store file URL in database
                blog_post = Blog.objects.create(
                    title=title,
                    author=author,
                    content=content,
                    image_url=image_url,
                )

                return Response({
                    'message': 'Blog added successfully', 
                    'data': { 
                        'title': title, 
                        'author': author, 
                        'content': content, 
                        'image_url': image_url, 
                        'pub_date': blog_post.pub_date.strftime('"%d/%m/%Y, %H:%M:%S"'), 
                        'updated_at': blog_post.updated_at.strftime('"%d/%m/%Y, %H:%M:%S"'), 
                    }
                }, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# Update a blog
class BlogUpdateView(generics.UpdateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


# Delete a blog
class BlogDeleteView(generics.DestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
