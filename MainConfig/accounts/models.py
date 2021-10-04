from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models


class UserAccountManager(BaseUserManager):
    def create_user(self, email, password=None,**extra_fields):
        if not email:
            raise ValueError("User must have an email address")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password,**extra_fields):
        user = self.create_user(email, password,**extra_fields)
        user.is_superuser = True
        user.is_staff = True
        user.is_active=True
        user.save()
        return user


class UserAccount(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=250, unique=True)
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    objects = UserAccountManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name','last_name']

    def get_full_name(self):
        return self.first_name

    def get_short_name(self):
        return self.first_name

    def get_user_id(self):
        return self.pk

    def get_short_name(self):
        return self.first_name

    def __str__(self):
        return self.email
