from django.db import models
from users.models import User

class Meal(models.Model):
    name = models.CharField(max_length=255)
    ingredients = models.TextField(null=False, blank=False)  # Yangi qo‘shilgan
    category = models.CharField(max_length=100, default='General')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='meals')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name