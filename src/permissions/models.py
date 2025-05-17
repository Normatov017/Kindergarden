from django.db import models

class Permission(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)  # optional: for tracking
    updated_at = models.DateTimeField(auto_now=True)      # optional: for updates

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'permissions'
        verbose_name = 'Permission'
        verbose_name_plural = 'Permissions'
        ordering = ['name']
