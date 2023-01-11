from rest_framework import serializers
from transport_orders.models import TransportOrder


class TransportOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransportOrder
        fields = '__all__'


class TransportOrderUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransportOrder
        fields = ['status', 'transport']
