from meals.models import Meal  # Recipe o‘rniga
from django.db import models
from users.models import User


class Servings(models.Model):
    recipe = models.ForeignKey(Meal, on_delete=models.CASCADE)  # Recipe emas
    served_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    served_at = models.DateTimeField()

    def __str__(self):
        return f"{self.recipe} served by {self.served_by}"
