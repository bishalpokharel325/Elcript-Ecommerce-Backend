from django.contrib import admin

# Register your models here.
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from .models import Order, OrderItem, Shipping


class orderResource(resources.ModelResource):
    class Meta:
        model = Order


class orderItemResource(resources.ModelResource):
    class Meta:
        model = OrderItem


class shippingResource(resources.ModelResource):
    class Meta:
        model = Shipping


@admin.register(Order)
class AdminOrder(ImportExportModelAdmin):
    resource_class = orderResource
    list_display = ['id', 'userId', 'date_ordered', 'status']
    search_fields = ['id', 'userId', 'date_ordered', 'status']
    date_hierarchy = 'date_ordered'
    list_per_page = 25


@admin.register(OrderItem)
class AdminOrderItem(ImportExportModelAdmin):
    resource_class = orderItemResource
    list_display = ["id",'orderId','quantity','date_added']
    search_fields = ["id",'orderId','quantity','date_added']
    date_hierarchy = 'date_added'
    list_per_page = 25


@admin.register(Shipping)
class AdminShipping(ImportExportModelAdmin):
    resource_class = shippingResource
    list_display = ["id",'orderId','address','city','state','zipcode','date_added']
    search_fields = ["id",'orderId','address','city','state','zipcode','date_added']
    date_hierarchy = 'date_added'
    list_per_page = 25

