from rest_framework import serializers
from .models import Product
from Supplier.serializers import SupplierSerializer

class ProductSerializer(serializers.ModelSerializer):
    supplier = SupplierSerializer(read_only=True)
    class Meta:
        model = Product
        fields = '__all__'