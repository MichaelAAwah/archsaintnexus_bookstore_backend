from django.urls import path
from .views import BlogListView, BlogDetailView
from . import views


urlpatterns = [
    path('', BlogListView.as_view(), name='blog-list'),
    path('<int:pk>/', BlogDetailView.as_view(), name='blog-detail'),


    # Endpoints for creating, updating, deleting, and viewings

    # Blog Endpoints
    path('', views.BlogListView.as_view(), name='blog-list'),
    path('create/', views.BlogCreateView.as_view(), name='blog-create'),
    path('<int:pk>/update/', views.BlogUpdateView.as_view(), name='blog-update'),
    path('<int:pk>/delete/', views.BlogDeleteView.as_view(), name='blog-delete'),
]