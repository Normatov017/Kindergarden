from django.db import models

class Group(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def kid_count(self):
        return self.kids.count()  # related_name='kids' orqali

class Kid(models.Model):
    STATUS_CHOICES = (
        ('active', 'Faol'),
        ('inactive', 'Nofaol'),
    )
    full_name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='kids')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)

    def __str__(self):
        return self.full_name
