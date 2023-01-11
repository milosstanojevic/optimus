from rest_framework import serializers
from merchant_articles.models import MerchantArticle


class MerchantArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = MerchantArticle
        fields = '__all__'
