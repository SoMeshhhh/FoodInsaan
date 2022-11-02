from dataclasses import fields
from rest_framework import serializers
from .models import FoodIssine

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodIssine
        fields = ['id','name','email','number']