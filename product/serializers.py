from rest_framework import serializers
from product.models import Category, Product, Review

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = 'id name'.split()

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

class CategoryValidateSerializer(serializers.Serializer):
    name = serializers.CharField(min_length=1, max_length=15)

class ProductValidateSerializer(serializers.Serializer):
    title = serializers.CharField( min_length=1, max_length=15)
    description = serializers.CharField(required=False)
    price = serializers.FloatField(min_value=1, max_value=5000)

class ReviewValidateSerializer(serializers.Serializer):
    text = serializers.CharField(min_length=15, max_length=100)
