from django.test import TestCase
from roles.models import Role
from permissions.models import Permission
from rolepermissions.models import RolePermission
from django.db import IntegrityError

class RolePermissionModelTest(TestCase):

    def setUp(self):
        self.role = Role.objects.create(name="Manager")
        self.permission = Permission.objects.create(name="Can View Reports")

    def test_create_role_permission(self):
        rp = RolePermission.objects.create(role=self.role, permission=self.permission)
        self.assertEqual(rp.role, self.role)
        self.assertEqual(rp.permission, self.permission)
        self.assertIsNotNone(rp.assigned_at)

    def test_str_method(self):
        rp = RolePermission.objects.create(role=self.role, permission=self.permission)
        expected_str = f"{self.role.name} -> {self.permission.name}"
        self.assertEqual(str(rp), expected_str)

    def test_unique_together_constraint(self):
        RolePermission.objects.create(role=self.role, permission=self.permission)
        with self.assertRaises(IntegrityError):
            RolePermission.objects.create(role=self.role, permission=self.permission)
