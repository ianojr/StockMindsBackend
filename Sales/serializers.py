from rest_framework import serializers
from .models import Sale
from Stock.serializers import StockSerializer
from User.views import UserSerializer

class SaleSerializer(serializers.ModelSerializer):
    stock = StockSerializer(read_only = True)
    sold_by = UserSerializer(read_only = True)
    class Meta:
        model = Sale
        fields = '__all__'