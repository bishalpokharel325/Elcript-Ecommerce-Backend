from django.db import models


# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=500, unique=True)
    visible = models.BooleanField(default=True)
    created_at = models.DateField(auto_now_add=True)
    created_by = models.ForeignKey('accounts.UserAccount', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.title


class Brand(models.Model):
    title = models.CharField(max_length=500, unique=True)
    visible = models.BooleanField(default=True)
    created_at = models.DateField(auto_now_add=True)
    created_by = models.ForeignKey('accounts.UserAccount', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.title
