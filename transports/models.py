from django.db import models

# Create your models here.


class Transport(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
