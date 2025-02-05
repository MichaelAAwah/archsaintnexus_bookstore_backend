from django.urls import path
from .views import BookListView, BookDetailView
from . import views


urlpatterns = [
    path('', BookListView.as_view(), name='book-list'),
    path('<int:pk>/', BookDetailView.as_view(), name='book-detail'),


    # Endpoints for creating, updating, deleting, and viewings

    # Book Endpoints
    path('', views.BookListView.as_view(), name='book-list'),
    path('create/', views.BookCreateView.as_view(), name='book-create'),
    path('<int:pk>/update/', views.BookUpdateView.as_view(), name='book-update'),
    path('<int:pk>/delete/', views.BookDeleteView.as_view(), name='book-delete'),
]