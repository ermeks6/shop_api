from rest_framework import serializers
from .models import Category, Product, Review, Tag
from rest_framework.exceptions import ValidationError


class CategorySerializer(serializers.ModelSerializer):
    products_count = serializers.SerializerMethodField()

    def get_products_count(self, obj):
        return obj.products.count()

    class Meta:
        model = Category
        fields = ['id', 'name', 'products_count']


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    avg_rating = serializers.FloatField(read_only=True)
    tags = TagSerializer(many=True)

    def validate_tags(value):
        existing_tags = Tag.objects.values_list('name', flat=True)
        for tag in value:
            if tag['name'] not in existing_tags:
                raise serializers.ValidationError(f"Tag '{tag['name']}' does not exist.")
        return value

    class Meta:
        model = Product
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

