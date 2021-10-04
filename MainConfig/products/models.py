from django.db import models

# Create your models here.
from django.db import models


# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=200, unique=True)
    description = models.TextField()
    category = models.ForeignKey('categorys.Category', on_delete=models.SET_NULL, null=True, blank=True)
    brand = models.ForeignKey('categorys.Brand', on_delete=models.SET_NULL, null=True, blank=True)
    created_by = models.ForeignKey('accounts.UserAccount', on_delete=models.SET_NULL, null=True, blank=True)
    price = models.DecimalField(decimal_places=2, max_digits=20)
    image = models.ImageField(upload_to="product_images/%Y/%m/%d")
    visible = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    cash_on_delivery = models.BooleanField(default=False)
    free_shipping = models.BooleanField(default=False)
    warranty_years = models.PositiveIntegerField(default=0)
    discount_price = models.DecimalField(decimal_places=2, max_digits=20, null=True, blank=True)
    discount_expiry = models.DateTimeField(null=True, blank=True)
    color_family = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return self.title
