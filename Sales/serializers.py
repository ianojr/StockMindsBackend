from rest_framework import serializers
from .models import Sale
from Stock.models import Stock
from Stock.serializers import StockSerializer
from User.views import UserSerializer

# class SaleSerializer(serializers.ModelSerializer):
#     stock = StockSerializer(read_only = True)
#     sold_by = UserSerializer(read_only = True)
#     class Meta:
#         model = Sale
#         fields = '__all__'

class SaleSerializer(serializers.ModelSerializer):
    stock = StockSerializer(read_only=True)
    sold_by = UserSerializer(read_only=True)

    stock_id = serializers.PrimaryKeyRelatedField(
        queryset=Stock.objects.all(),
        source='stock',
        write_only=True
    )

    class Meta:
        model = Sale
        fields = ['id', 'stock', 'stock_id', 'sold_by', 'quantity', 'total_price', 'time']
        extra_kwargs = {
            'sold_by': {'read_only': True},
            'time': {'read_only': True},
        }

