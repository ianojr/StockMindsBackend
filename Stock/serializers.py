from rest_framework import serializers
from .models import Stock
from Product.serializers import ProductSerializer
from User.views import UserSerializer

class StockSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only = True)
    added_by = UserSerializer(read_only = True)
    class Meta:
        model = Stock
        fields = '__all__'