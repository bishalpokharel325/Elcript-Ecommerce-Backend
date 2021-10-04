from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Order, OrderItem, Shipping
from .serializers import OrderSerializer, OrderItemSerializer, ShippingSerializer
from django.apps import apps


def get_price_from_id(id):
    products = apps.get_app_config("products")
    Product = products.models['product']
    queryset_products = Product.objects.filter().order_by("id").values('id', 'price')
    for queryset_product in queryset_products:
        if queryset_product['id'] == id:
            return queryset_product['price']
    return None


@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def get_orders(request, uid):
    status = request.GET.get('status')
    if request.method == 'GET':
        queryset = Order.objects.filter(userId=uid)
        if status:
            queryset=queryset.filter(status=status)
        serializer = OrderSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response({"error": "data not found"}, status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def post_orders(request):
    if request.method == 'POST':
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT', 'GET', 'DELETE'])
@permission_classes((IsAuthenticated,))
def put_single_order(request, uid, id):
    try:
        order = Order.objects.get(pk=id, userId=uid)
    except order.DoesNotExist:
        return Response({"error": "Order Not Found"}, status=status.HTTP_404_NOT_FOUND)
    if request.method == 'PUT':
        serializer = OrderSerializer(order, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'GET':
        serializer = OrderSerializer(order, many=True)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def get_orderItems(request, uid):
    total_items = 0
    total_price = 0
    order_id = request.GET.get('order_id')
    if request.method == 'GET':
        queryset = OrderItem.objects.filter(userId=uid)
        if order_id:
            queryset = queryset.filter(orderId_id=order_id)
        for query in queryset.values():
            price = get_price_from_id(query['productId_id'])
            total_price = total_price + price * query['quantity']
            total_items = query['quantity'] + total_items

        serializer = OrderItemSerializer(queryset, many=True)
        return Response({"orderItems": serializer.data, "total_items": total_items, 'total_price': total_price},
                        status=status.HTTP_200_OK)
    else:
        return Response({"error": "data not found"}, status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def post_orderItems(request):
    if request.method == 'POST':
        serializer = OrderItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
@permission_classes((IsAuthenticated,))
def put_single_orderItems(request, uid, id):
    try:
        order = OrderItem.objects.get(pk=id, userId=uid)
    except order.DoesNotExist:
        return Response({"error": "Order Not Found"}, status=status.HTTP_404_NOT_FOUND)
    if request.method == 'PUT':
        serializer = OrderItemSerializer(order, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'GET':
        serializer = OrderItemSerializer(order)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def get_shipping(request, uid):
    if request.method == 'GET':
        queryset = Shipping.objects.filter(userId=uid)
        serializer = ShippingSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response({"error": "data not found"}, status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def post_shipping(request):
    if request.method == 'POST':
        serializer = ShippingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
@permission_classes((IsAuthenticated,))
def put_single_shipping(request, uid, id):
    try:
        ship = Shipping.objects.get(pk=id, userId=uid)
    except ship.DoesNotExist:
        return Response({"error": "Shipping Data Not Found"}, status=status.HTTP_404_NOT_FOUND)
    if request.method == 'PUT':
        serializer = ShippingSerializer(ship, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'GET':
        serializer = ShippingSerializer(ship)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        ship.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
