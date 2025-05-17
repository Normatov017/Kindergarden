from django.test import TestCase
from roles.models import Role
from users.models import user
from meals.models import Meal

class MealModelTest(TestCase):

    def setUp(self):
        # Test uchun kerakli Role va user yaratamiz
        self.role = Role.objects.create(name="Chef")
        self.user_instance = user.objects.create(
            username="chefuser",
            full_name="Chef User",
            password_hash="secure123",
            role=self.role
        )

    def test_create_meal(self):
        meal = Meal.objects.create(
            name="Plov",
            category="Main Dish",
            created_by=self.user_instance
        )
        self.assertEqual(meal.name, "Plov")
        self.assertEqual(meal.category, "Main Dish")
        self.assertEqual(meal.created_by, self.user_instance)
        self.assertIsNotNone(meal.created_at)

    def test_str_method(self):
        meal = Meal.objects.create(
            name="Lagman",
            category="Soup",
            created_by=self.user_instance
        )
        self.assertEqual(str(meal), "Lagman")
