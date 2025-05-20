from django.db import models
from roles.models import Role  # Role modelini import qilamiz
from django.contrib.auth.models import AbstractUser
class User(AbstractUser):
    full_name = models.CharField(max_length=255)
    role = models.ForeignKey(Role, on_delete=models.CASCADE, related_name='users',blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'users'
        verbose_name = 'User'
        verbose_name_plural = 'Users'
