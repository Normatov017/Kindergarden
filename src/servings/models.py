from django.db import models
from users.models import User
from recipes.models import Recipe

class Servings(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    served_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    served_at = models.DateTimeField()

    def __str__(self):
        return f"{self.recipe} served by {self.served_by}"
