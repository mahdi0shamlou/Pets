from rest_framework import serializers
from .models import Animals


class AnimalsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Animals
        fields = ['id', 'name', 'date_added', 'price', 'is_active']