from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.


class CustomUser(AbstractUser):
    address = models.CharField(null=True, blank=True, max_length=30)
    phone = models.CharField(null=True, blank=True, unique=True, max_length=12)
    age = models.PositiveIntegerField(null=True, blank=True)
    first_name = models.CharField(null=True, blank=True, max_length=15)
    last_name = models.CharField(null=True, blank=True, max_length=15)
