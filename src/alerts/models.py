from django.db import models
from products.models import Product

class Alerts(models.Model):
    ALERT_TYPES = [
        ('LOW_STOCK', 'Low Stock'),
        ('EXPIRY_SOON', 'Expiry Soon'),
        ('GENERAL', 'General'),
    ]

    alert_type = models.CharField(max_length=20, choices=ALERT_TYPES)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.alert_type} - {self.product}"
