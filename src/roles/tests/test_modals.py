from django.test import TestCase
from roles.models import Role
from django.db import IntegrityError

class RoleModelTest(TestCase):

    def setUp(self):
        self.role = Role.objects.create(
            name="Admin",
            description="Administrator role"
        )

    def test_role_creation(self):
        self.assertEqual(self.role.name, "Admin")
        self.assertEqual(self.role.description, "Administrator role")
        self.assertIsNotNone(self.role.created_at)

    def test_role_str_method(self):
        self.assertEqual(str(self.role), "Admin")

    def test_role_unique_name(self):
        # Duplicate role with same name should raise IntegrityError
        with self.assertRaises(IntegrityError):
            Role.objects.create(name="Admin")

    def test_blank_description(self):
        role = Role.objects.create(name="Editor")
        self.assertEqual(role.description, None)
