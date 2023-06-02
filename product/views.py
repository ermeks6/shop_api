from django.db.models import Avg
from rest_framework import generics
from .models import Category, Product, Review, Tag
from .serializers import CategorySerializer, ProductSerializer, ReviewSerializer, TagSerializer
from django.db import models
from rest_framework import status


class CategoryListAPIView(generics.ListCreateAPIView):
    queryset = Category.objects.annotate(products_count=models.Count('products'))
    serializer_class = CategorySerializer


class CategoryDetailAPIView(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def create(self, request, *args, **kwargs):
        tags_data = request.data.get('tags', [])
        tags_serializer = TagSerializer(data=tags_data, many=True)
        tags_serializer.is_valid(raise_exception=True)
        tags = tags_serializer.save()
        request.data['tags'] = [tag.pk for tag in tags]
        return super().create(request, *args, **kwargs)

    def perform_create(self, serializer):
        tags_data = self.request.data.get('tags', [])
        tags = Tag.objects.filter(pk__in=tags_data)
        serializer.save(tags=tags)


class ProductListAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.annotate(avg_rating=Avg('review__stars'))
    serializer_class = ProductSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['include_reviews'] = True
        return context

    class ProductDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
        queryset = Product.objects.all()
        serializer_class = ProductSerializer

        def perform_update(self, serializer):
            tags_data = self.request.data.get('tags', [])
            tags = Tag.objects.filter(pk__in=tags_data)
            serializer.save(tags=tags)

        def perform_destroy(self, instance):
            instance.tags.clear()
            instance.delete()


class ReviewListAPIView(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class ReviewDetailAPIView(generics.RetrieveAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


