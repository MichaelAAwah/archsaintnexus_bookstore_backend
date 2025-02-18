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
                book = Book.objects.create(
                    book_name=book_name,
                    author=author,
                    price=price,
                    image_url=image_url,
                    release_date=release_date,
                    pub_date=pub_date,
                )
                print(book)

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
    # queryset = Book.objects.all()
    # serializer_class = BookSerializer
    # permission_classes = [IsAuthenticatedOrReadOnly]

    def put(self, request, *args, **kwargs):
        book_id = kwargs.get("pk")
        book = Book.objects.get(id=book_id)

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
                
                for field, value in serializer.validated_data.items():
                    if field == "image":
                        book.image_url = image_url
                    else:
                        setattr(book, field, value) 

                book.save()

                return Response({
                    'message': 'Book updated successfully', 
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

    def patch(self, request, *args, **kwargs):
        book_id = kwargs.get("pk")
        book = Book.objects.get(id=book_id)

        serializer = BookSerializer(book, data=request.data, partial=True)
        if serializer.is_valid():
           
            for field, value in serializer.validated_data.items():
                if field == "image":
                    upload_result = cloudinary.uploader.upload(value)
                    book.image_url = upload_result.get("secure_url", book.image_url)
                else:
                    setattr(book, field, value) 

            book.save()

            return Response({
                "message": "Book updated successfully",
                "data": {
                    "book_name": book.book_name,
                    "author": book.author,
                    "price": float(book.price),
                    "image_url": book.image_url,
                    "release_date": book.release_date,
                    "pub_date": book.pub_date
                }
            }, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# Delete a book
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    # permission_classes = [IsAuthenticatedOrReadOnly]
