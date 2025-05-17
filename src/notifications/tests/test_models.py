from django.test import TestCase
from roles.models import Role
from users.models import user
from notifications.models import Notification

class NotificationModelTest(TestCase):

    def setUp(self):
        self.role = Role.objects.create(name="User")
        self.user_instance = user.objects.create(
            username="testuser",
            full_name="Test User",
            password_hash="hashed_pass",
            role=self.role
        )

    def test_create_notification(self):
        notif = Notification.objects.create(
            user=self.user_instance,
            message="Welcome to the system!"
        )
        self.assertEqual(notif.user, self.user_instance)
        self.assertEqual(notif.message, "Welcome to the system!")
        self.assertFalse(notif.is_read)
        self.assertIsNotNone(notif.created_at)

    def test_str_method(self):
        notif = Notification.objects.create(
            user=self.user_instance,
            message="You have a new message."
        )
        self.assertEqual(str(notif), f"Notification to {self.user_instance.username}")
