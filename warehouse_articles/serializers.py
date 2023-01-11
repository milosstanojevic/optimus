from rest_framework import serializers
from warehouse_articles.models import WarehouseArticle


class WarehouseArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = WarehouseArticle
        fields = '__all__'
