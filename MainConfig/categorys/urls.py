from django.urls import path

from . import views

urlpatterns=[
    path("get-categories",views.get_categories,name="get_categories"),
    path("get-categories/<int:id>",views.get_single_category,name="get_single_category"),
    path("post-categories",views.post_categories,name="post_categories"),
    path("put-categories/<int:id>",views.put_category,name="put_category"),

    path("get-brands",views.get_brands,name="get_brands"),
    path("get-brands/<int:id>",views.get_single_brand,name="get_single_brand"),
    path("post-brands",views.post_brand,name="post_brands"),
    path("put-brands/<int:id>",views.put_brand,name="put_brand"),
]