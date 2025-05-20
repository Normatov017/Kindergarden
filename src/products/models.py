from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    weight = models.DecimalField(max_digits=10, decimal_places=2)
    unit = models.CharField(max_length=50, default='gram')
    delivery_date = models.DateField()
    minimum_threshold = models.DecimalField(max_digits=10, decimal_places=2, default=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    quantity = models.BigIntegerField(null=False, blank=False, default=0)

    def __str__(self):
        return self.name
