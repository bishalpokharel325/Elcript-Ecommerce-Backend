from django.db import models

# Create your models here.
PENDING = "pending"
SHIPPING = "shipping"
COMPLETED = "completed"
STATUS_CHOICE = (
    (PENDING, "pending"),
    (SHIPPING, "shipping"),
    (COMPLETED, "completed"),
)


class Order(models.Model):
    userId = models.ForeignKey('accounts.UserAccount', on_delete=models.SET_NULL, null=True, blank=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    status = models.CharField(choices=STATUS_CHOICE, max_length=20, default=PENDING)

    def __str__(self):
        return f"{self.pk}"


class OrderItem(models.Model):
    userId = models.ForeignKey('accounts.UserAccount', on_delete=models.SET_NULL, null=True, blank=True)
    productId = models.ForeignKey('products.Product', on_delete=models.SET_NULL, null=True, blank=True)
    orderId = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, blank=True)
    quantity = models.PositiveIntegerField(default=0)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.pk}'


class Shipping(models.Model):
    userId = models.ForeignKey('accounts.UserAccount', on_delete=models.SET_NULL, null=True, blank=True)
    orderId = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    city = models.CharField(max_length=200, null=True, blank=True)
    state = models.CharField(max_length=200, null=True, blank=True)
    zipcode = models.CharField(max_length=200, null=True, blank=True)
    phoneno = models.CharField(max_length=200, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Shipping Id{self.pk}"
