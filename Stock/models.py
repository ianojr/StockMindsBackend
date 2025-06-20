from django.db import models
from django.contrib.auth import get_user_model
from Product.models import Product  # adjust this if needed

User = get_user_model()

class Stock(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity_added = models.PositiveIntegerField()
    added_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    note = models.TextField(blank=True)

    def __str__(self):
        return f"Restocked {self.product.name} by {self.quantity_added} units"
