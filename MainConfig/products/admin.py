from django.contrib import admin

# Register your models here.
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from .models import Product


class productResource(resources.ModelResource):
    class Meta:
        model = Product


@admin.register(Product)
class AdminProduct(ImportExportModelAdmin):
    resource_class = productResource
    list_display = ['title', 'price', 'created_at', 'visible', 'created_by']
    search_fields = ['title', 'description', 'price', 'visible', 'created_at']
    date_hierarchy = 'created_at'
    list_per_page = 10
    exclude = ['created_by']



