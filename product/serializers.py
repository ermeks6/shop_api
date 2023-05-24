from rest_framework import serializers
from .models import Category, Product, Review


class CategorySerializer(serializers.ModelSerializer):
    products_count = serializers.SerializerMethodField()

    def get_products_count(self, obj):
        return obj.products.count()  # Use 'products' instead of 'product_set'

    class Meta:
        model = Category
        fields = ['id', 'name', 'products_count']


class ProductSerializer(serializers.ModelSerializer):
    avg_rating = serializers.FloatField(read_only=True)

    class Meta:
        model = Product
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

