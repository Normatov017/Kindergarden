# main/models.py
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.IntegerField(default=0)

class Meal(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField(auto_now_add=True)

class PortionServed(models.Model):
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)
    count = models.PositiveIntegerField()
    served_at = models.DateField(auto_now_add=True)
