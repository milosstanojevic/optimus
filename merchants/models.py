from django.db import models

# Create your models here.


class Merchant(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True)
    address = models.CharField(max_length=200)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
