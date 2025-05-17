from django.test import TestCase
from roles.models import Role
from users.models import user

class UserModelTest(TestCase):

    def setUp(self):
        self.role = Role.objects.create(name="Admin")

    def test_create_user(self):
        usr = user.objects.create(
            username="azizbek01",
            full_name="Azizbek Qodiraliyev",
            password_hash="hashed_password_example",
            role=self.role
        )
        self.assertEqual(usr.username, "azizbek01")
        self.assertEqual(usr.full_name, "Azizbek Qodiraliyev")
        self.assertEqual(usr.role, self.role)
        self.assertIsNotNone(usr.created_at)

    def test_str_method(self):
        usr = user.objects.create(
            username="johndoe",
            full_name="John Doe",
            password_hash="hashed_password",
            role=self.role
        )
        self.assertEqual(str(usr), "johndoe")
