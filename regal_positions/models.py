from django.db import models
from regals.models import Regal

# Create your models here.


class RegalPosition(models.Model):
    name = models.CharField(max_length=200)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    regal = models.ForeignKey(Regal, on_delete=models.CASCADE)
