from rest_framework import serializers
from .models import Brand, Mobile


class WarehouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mobile
        fields = '__all__'
