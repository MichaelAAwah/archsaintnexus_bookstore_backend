from django.shortcuts import render
from rest_framework import generics, filters
from .models import Book
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
import cloudinary.uploader
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class BookListView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['book_name', 'author']
    ordering_fields = ['book_name']


class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['book_name', 'author']
    ordering_fields = ['book_name', 'price', 'release_date', 'pub_date']


# Endpoints for creating, updating, deleting, and viewings

# Books
class BookCreateView(generics.CreateAPIView):
    # queryset = Book.objects.all()
    # serializer_class = BookSerializer
    # permission_classes = [IsAuthenticatedOrReadOnly]

    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            book_name = serializer.validated_data['book_name']
            author = serializer.validated_data['author']
            price = serializer.validated_data['price']
            image = serializer.validated_data['image']
            release_date = serializer.validated_data['release_date']
            pub_date = serializer.validated_data['pub_date']

            # Upload to Cloudinary
            upload_result = cloudinary.uploader.upload(image)

            if 'secure_url' in upload_result:
                image_url = upload_result['secure_url']
                
                # Store file URL in database
                print(request.data)
                uploaded_file = Book.objects.create(
                    book_name=book_name,
                    author=author,
                    price=price,
                    image_url=image_url,
                    release_date=release_date,
                    pub_date=pub_date,
                )
                print(uploaded_file)

                return Response({
                    'message': 'Book added successfully', 
                    'data': { 
                        'book_name': book_name, 
                        'author': author, 
                        'price': float(price), 
                        'image_url': image_url, 
                        'release_date': release_date, 
                        'pub_date': pub_date 
                    }
                }, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# Update a book
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


# Delete a book
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
