from django.urls import path

from . import views

urlpatterns=[
    path("get-orders/<int:uid>",views.get_orders,name="get_orders"),
    path("post-orders",views.post_orders,name="post_orders"),
    path("put-orders/<int:uid>/<int:id>",views.put_single_order,name="put_single_Orders"),
    path("get-orderItems/<int:uid>",views.get_orderItems,name="get_Items"),
    path("post-orderItems",views.post_orderItems,name="post_Items"),
    path("put-orderItems/<int:uid>/<int:id>",views.put_single_orderItems,name="put_single_Items"),
    path("get-shipping",views.get_shipping,name="get_Shipping"),
    path("post-shipping",views.post_shipping,name="post_Shipping"),
    path("put-shipping/<int:uid>/<int:id>",views.put_single_shipping,name="put_single_shipping"),
]