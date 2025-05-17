from django.db import models
from recipes.models import Recipe

class PortionEstimate(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='portion_estimates')
    possible_portions = models.IntegerField()
    calculated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Estimates for {self.recipe.id}"