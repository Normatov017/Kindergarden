from django.db import models
from products.models import Product
from users.models import user

class Inventory(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='inventories')
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    delivery_date = models.DateField()
    expiry_date = models.DateField()
    source = models.CharField(max_length=255)
    created_by = models.ForeignKey(user, on_delete=models.CASCADE, related_name='inventory_records')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.product.name} - {self.quantity}"