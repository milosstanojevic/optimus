from rest_framework import serializers
from transport_articles.models import TransportArticle
from warehouses.models import Warehouse
from regals.models import Regal
from regal_positions.models import RegalPosition


class WarehouseRelationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Warehouse
        fields = ['id', 'name']


class RegalRelationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Regal
        fields = ['id', 'name']


class RegalPositionRelationSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegalPosition
        fields = ['id', 'name']


class TransportArticleListSerializer(serializers.ModelSerializer):
    warehouse = WarehouseRelationSerializer(read_only=True)
    regal = RegalRelationSerializer(read_only=True)
    regal_position = RegalPositionRelationSerializer(read_only=True)

    class Meta:
        model = TransportArticle
        fields = '__all__'


class TransportArticleSerializer(serializers.ModelSerializer):

    class Meta:
        model = TransportArticle
        fields = '__all__'
