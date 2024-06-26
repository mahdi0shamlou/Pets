from rest_framework import serializers
from .models import Animals, AnimalsUsers


class AnimalsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Animals
        fields = ['id', 'name', 'date_added', 'price', 'is_active']


class AnimalsUsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnimalsUsers
        fields = ['id', 'name', 'date_added', 'user', 'type', 'age']
