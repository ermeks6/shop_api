from django.urls import path
from .views import CategoryListAPIView, CategoryDetailAPIView, ProductListAPIView, ProductDetailAPIView, ReviewListAPIView, ReviewDetailAPIView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import RegisterUserView, ConfirmUserView

app_name = 'product'

urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('users/confirm/', ConfirmUserView.as_view(), name='confirm_user'),
    path('categories/', CategoryListAPIView.as_view(), name='category-list'),
    path('categories/<int:pk>/', CategoryDetailAPIView.as_view(), name='category-detail'),
    path('products/', ProductListAPIView.as_view(), name='product-list'),
    path('products/<int:pk>/', ProductDetailAPIView.as_view(), name='product-detail'),
    path('reviews/', ReviewListAPIView.as_view(), name='review-list'),
    path('reviews/<int:pk>/', ReviewDetailAPIView.as_view(), name='review-detail'),
]
