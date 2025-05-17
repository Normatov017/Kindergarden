from django.db import models
from servings.models import Servings
from products.models import Product

class ServingLogs(models.Model):
    serving = models.ForeignKey(Servings, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity_used = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.serving} - {self.product} used"
