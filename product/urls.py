from django.urls import path
from .views import CategoryListAPIView, CategoryDetailAPIView, ProductListAPIView, ProductDetailAPIView, ReviewListAPIView, ReviewDetailAPIView

app_name = 'product'

urlpatterns = [
    path('categories/', CategoryListAPIView.as_view(), name='category-list'),
    path('categories/<int:pk>/', CategoryDetailAPIView.as_view(), name='category-detail'),
    path('products/', ProductListAPIView.as_view(), name='product-list'),
    path('products/<int:pk>/', ProductDetailAPIView.as_view(), name='product-detail'),
    path('reviews/', ReviewListAPIView.as_view(), name='review-list'),
    path('reviews/<int:pk>/', ReviewDetailAPIView.as_view(), name='review-detail'),
]
