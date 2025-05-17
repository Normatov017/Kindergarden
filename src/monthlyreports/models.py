from django.db import models

class MonthlyReports(models.Model):
    month_year = models.CharField(max_length=7)  # Format: YYYY-MM
    total_served = models.IntegerField()
    total_possible = models.IntegerField()
    difference_percent = models.DecimalField(max_digits=5, decimal_places=2)
    generated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Report for {self.month_year}"
