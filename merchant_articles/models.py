from django.db import models
from articles.models import Article
from merchants.models import Merchant

# Create your models here.


class MerchantArticle(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    merchant = models.ForeignKey(Merchant, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
