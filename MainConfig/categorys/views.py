from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Category, Brand
from .serializers import CategorySerializer, BrandSerializer


@api_view(['GET'])
def get_categories(request):
    if request.method == 'GET':
        queryset = Category.objects.filter(visible=True).order_by("-created_at")
        serializer = CategorySerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response({"error": "data not found"}, status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def get_single_category(request, id):
    try:
        category = Category.objects.get(pk=id)
    except category.DoesNotExist:
        return Response({"error": "Category Not Found"},status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        queryset = Category.objects.filter(visible=True).filter(pk=id).order_by("-created_at")
        serializer = CategorySerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response({"error": "data not found"}, status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def post_categories(request):
    if request.method == 'POST':
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
@permission_classes((IsAuthenticated,))
def put_category(request, id):
    try:
        category = Category.objects.get(pk=id)
    except category.DoesNotExist:
        return Response({"error": "Category Not Found"},status=status.HTTP_404_NOT_FOUND)
    if request.method == 'PUT':
        serializer = CategorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_brands(request):
    if request.method == 'GET':
        queryset = Brand.objects.filter(visible=True).order_by("-created_at")
        serializer = BrandSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response({"error": "data not found"}, status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def get_single_brand(request, id):
    try:
        brand = Brand.objects.get(pk=id)
    except brand.DoesNotExist:
        return Response({"error": "Brand Not Found"},status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        queryset = Brand.objects.filter(visible=True).filter(pk=id).order_by("-created_at")
        serializer = BrandSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response({"error": "data not found"}, status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def post_brand(request):
    if request.method == 'POST':
        serializer = BrandSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
@permission_classes((IsAuthenticated,))
def put_brand(request, id):
    try:
        brand = Brand.objects.get(pk=id)
    except brand.DoesNotExist:
        return Response({"error": "Category Not Found"},status=status.HTTP_404_NOT_FOUND)
    if request.method == 'PUT':
        serializer = BrandSerializer(brand, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
