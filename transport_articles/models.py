from django.db import models
from articles.models import Article
from warehouses.models import Warehouse
from regals.models import Regal
from regal_positions.models import RegalPosition
from transport_order_articles.models import TransportOrderArticle
from warehouse_articles.models import WarehouseArticle
from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete

# Create your models here.


class TransportArticle(models.Model):
    transport_order_article = models.ForeignKey(
        TransportOrderArticle, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE)
    regal = models.ForeignKey(Regal, on_delete=models.CASCADE)
    regal_position = models.ForeignKey(RegalPosition, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)


@receiver(post_save, sender=TransportArticle)
def transport_article_post_save_handler(sender, instance, created, *args, **kwargs):
    warehouse_article = WarehouseArticle.objects.get(
        article=instance.article, warehouse=instance.warehouse, regal=instance.regal, regal_position=instance.regal_position)
    transport_order_article = TransportOrderArticle.objects.get(
        id=instance.transport_order_article.id)
    if transport_order_article is not None:
        quantity = instance.quantity
        if transport_order_article.transport_quantity is not None:
            quantity = transport_order_article.transport_quantity + instance.quantity
        transport_order_article.transport_quantity = quantity
        transport_order_article.save()
    if warehouse_article is not None:
        warehouse_article.quantity = warehouse_article.quantity - instance.quantity
        warehouse_article.save()


@receiver(post_delete, sender=TransportArticle)
def transport_article_post_delete_handler(sender, instance, *args, **kwargs):
    warehouse_article = WarehouseArticle.objects.get(
        article=instance.article, warehouse=instance.warehouse, regal=instance.regal, regal_position=instance.regal_position)
    transport_order_article = TransportOrderArticle.objects.get(
        id=instance.transport_order_article.id)
    if transport_order_article is not None:
        quantity = instance.quantity
        if transport_order_article.transport_quantity is not None:
            quantity = transport_order_article.transport_quantity - instance.quantity
        transport_order_article.transport_quantity = quantity
        transport_order_article.save()
    if warehouse_article is not None:
        warehouse_article.quantity = warehouse_article.quantity + instance.quantity
        warehouse_article.save()
