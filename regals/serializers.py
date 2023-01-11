from rest_framework import serializers
from regals.models import Regal


class RegalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Regal
        fields = '__all__'
