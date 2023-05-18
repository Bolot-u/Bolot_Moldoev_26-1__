from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from product.serializers import CategorySerializer, ProductSerializer, ReviewSerializer, CategoryValidateSerializer, \
    ProductValidateSerializer, ReviewValidateSerializer
from product.models import Category, Product, Review

@api_view(['GET', 'POST'])
def category_list_api_view(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        data_dict = CategorySerializer(instance=categories, many=True).data

        return Response(data=data_dict)
    elif request.method == 'POST':
        serializer = CategoryValidateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)
        name = serializer.validated_data.get('name')
        categories = Category.objects.create(name=name)
        return Response(data=CategorySerializer(categories).data)

@api_view(['GET','PUT','DELETE'])
def category_detail_api_view(request, id):
    try:
        category = Category.objects.get(id=id)
    except Category.DoesNotExist:
        return Response(data={'error': 'Category not found'},
                        status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        data_dict = CategorySerializer(category, many=False).data
        return Response(data=data_dict)
    elif request.method == 'DELETE':
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'PUT':
        serializer = CategoryValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        category.name = serializer.validated_data.get('name')
        category.save()

        return Response(data=CategorySerializer(category).data)


@api_view(['GET','POST'])
def product_list_api_view(request):
    if request.method == 'GET':
        products = Product.objects.all()
        data_dict = ProductSerializer(products, many=True).data
        return Response(data=data_dict)
    elif request.method == 'POST':
        serializer = ProductValidateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)
        title = serializer.validated_data.get('title')
        description = serializer.validated_data.get('description')
        price = serializer.validated_data.get('price')
        product = Product.objects.create(title=title, description=description, price=price)
        return Response(data=ProductSerializer(product).data)
@api_view(['GET','PUT','DELETE'])
def product_detail_api_view(request, id):
    try:
        product = Product.objects.get(id=id)
    except Product.DoesNotExist:
        return Response(data={'error': 'Product not found'},
                        status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        data_dict = ProductSerializer(product, many=False).data
        return Response(data=data_dict)
    elif request.method == 'DELETE':
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'PUT':
        serializer = ProductValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        product.title = serializer.validated_data.get('title')
        product.description = serializer.validated_data.get('description')
        product.price = serializer.validated_data.get('price')
        product.save()
        return Response(data=ProductSerializer(product).data)



@api_view(['GET','POST'])
def review_list_api_view(request):
    if request.method == 'GET':
        reviews = Review.objects.all()
        data_dict = ReviewSerializer(reviews, many=True).data
        return Response(data=data_dict)
    elif request.method == 'POST':
        serializer = ReviewValidateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)
        text = serializer.validated_data.get('text')
        review = Review.objects.create(text=text)
        return Response(data=CategorySerializer(review).data)

@api_view(['GET','PUT','DELETE'])
def review_detail_api_view(request, id):
    try:
        review = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(data={'error': 'Review not found'},
                        status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        data_dict = ReviewSerializer(review, many=False).data
        return Response(data=data_dict)
    elif request.method == 'DELETE':
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'PUT':
        serializer = ReviewValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        review.text = serializer.validated_data.get('review')
        review.save()
        return Response(data=CategorySerializer(review).data)




@api_view(['GET'])
def test_api_view(request):
    data_dict = {
        "text": "Hello World!"
    }
    return Response(data=data_dict
                    )
# Create your views here.
