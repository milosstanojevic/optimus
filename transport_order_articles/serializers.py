from rest_framework import serializers
from transport_order_articles.models import TransportOrderArticle


class TransportOrderArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransportOrderArticle
        fields = '__all__'


class TransportOrderArticleStockSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransportOrderArticle
        fields = ['status']
