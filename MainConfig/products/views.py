from django.shortcuts import render
import datetime
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer
from django.db.models import Q


@api_view(['GET'])
def get_products(request):
    if request.method == 'GET':
        queryset = Product.objects.filter(visible=True).order_by("-created_at")
        brand_id = request.GET.get('brand_id')
        cash_on_delivery = request.GET.get('cash_on_delivery')
        free_shipping = request.GET.get('free_shipping')
        price_min = request.GET.get('price_min')
        price_max = request.GET.get('price_max')
        color_family = request.GET.get('color_family')
        warranty_years = request.GET.get('warranty_years')
        discount = request.GET.get('discount')
        sort_by = request.GET.get('sort_by')
        sort_direction = request.GET.get('sort_direction')
        category_id = request.GET.get('category_id')
        keyword = request.GET.get('keyword')
        if keyword:
            queryset = queryset.filter(
                Q(title__icontains=keyword) | Q(description__icontains=keyword) | Q(color_family__icontains=keyword))
        if discount:
            queryset = queryset.filter(discount_expiry__lt=datetime.now())
        if color_family:
            queryset = queryset.filter(color_family__iexact=color_family)
        if warranty_years:
            queryset = queryset.filter(warranty_years__gte=int(warranty_years))
        if cash_on_delivery:
            queryset = queryset.filter(cash_on_delivery=True)
        if free_shipping:
            queryset = queryset.filter(free_shipping=True)
        if brand_id:
            queryset = queryset.filter(brand_id=brand_id)
        if category_id:
            queryset = queryset.filter(category_id=category_id)
        if price_min:
            queryset = queryset.filter(price__gte=price_min)
        if price_max:
            queryset = queryset.filter(price__lte=price_max)
        if sort_by and sort_direction:
            if int(sort_direction) == 1:
                queryset = queryset.filter().order_by(f'{sort_by}')
            if int(sort_direction) == -1:
                queryset = queryset.filter().order_by(f'-{sort_by}')
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def post_products(request):
    if request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes((AllowAny,))
def get_single_product(request, id):
    try:
        product = Product.objects.get(pk=id)
    except product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ProductSerializer(product)
        return Response(serializer.data)


@api_view(['PUT'])
@permission_classes((IsAuthenticated,))
def put_single_product(request, id):
    try:
        product = Product.objects.get(pk=id)
    except product.DoesNotExist:
        return Response({"error": "Product Not Found"}, status=status.HTTP_404_NOT_FOUND)
    if request.method == 'PUT':
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

