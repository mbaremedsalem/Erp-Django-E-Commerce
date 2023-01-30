from rest_framework import serializers
from .models import Product

class shopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__' 