from rest_framework import serializers

from .models import Order, OrderItem, Shipping


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = "__all__"


class ShippingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shipping
        fields = "__all__"
