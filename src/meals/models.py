from django.db import models
from users.models import user

class Meal(models.Model):
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=100)
    created_by = models.ForeignKey(user, on_delete=models.CASCADE, related_name='meals')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name