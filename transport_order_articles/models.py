from django.db import models
from articles.models import Article
from transport_orders.models import TransportOrder

# Create your models here.


class TransportOrderArticle(models.Model):
    pending = '1'
    added = '2'

    STATUS_CHOICES = [
        (pending, 'Pending'),
        (added, 'Added'),
    ]

    transport_order = models.ForeignKey(
        TransportOrder, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    requested_quantity = models.PositiveIntegerField()
    transport_quantity = models.PositiveIntegerField(null=True)
    reason = models.TextField(null=True)
    status = models.CharField(
        max_length=2, choices=STATUS_CHOICES, default=pending)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
