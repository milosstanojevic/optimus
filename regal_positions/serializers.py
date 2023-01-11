from rest_framework import serializers
from regal_positions.models import RegalPosition


class RegalPositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegalPosition
        fields = '__all__'
