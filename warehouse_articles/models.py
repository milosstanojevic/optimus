from django.db import models
from articles.models import Article
from warehouses.models import Warehouse
from regals.models import Regal
from regal_positions.models import RegalPosition

# Create your models here.


class WarehouseArticle(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE)
    regal = models.ForeignKey(Regal, on_delete=models.CASCADE)
    regal_position = models.ForeignKey(RegalPosition, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
