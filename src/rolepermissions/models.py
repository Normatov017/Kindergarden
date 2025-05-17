from django.db import models
from permissions.models import Permission  # Import Permission model
from roles.models import Role              # Import Role model

class RolePermission(models.Model):
    role = models.ForeignKey(Role, on_delete=models.CASCADE, related_name='role_permissions')
    permission = models.ForeignKey(Permission, on_delete=models.CASCADE, related_name='permission_roles')

    assigned_at = models.DateTimeField(auto_now_add=True)  # optional: qachon biriktirilgan

    def __str__(self):
        return f"{self.role.name} -> {self.permission.name}"

    class Meta:
        db_table = 'role_permissions'
        unique_together = ('role', 'permission')
        verbose_name = 'Role Permission'
        verbose_name_plural = 'Role Permissions'
