from django.urls import path

from . import views

urlpatterns=[
    path("get-products",views.get_products,name="get_products"),
    path("post-products",views.post_products,name="post_products"),
    path("get-products/<int:id>",views.get_single_product,name="get_single_product"),
    path("put-products/<int:id>",views.put_single_product,name="get_single_category"),
]