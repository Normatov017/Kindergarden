# from django.contrib.auth import get_user_model
# from django.test import TestCase
# from meals.models import Meal
# from resipes.models import Recipe
#
# User = get_user_model()
#
# class RecipeModelTest(TestCase):
#     def setUp(self):
#         self.user = User.objects.create_user(username='testuser', password='password123')
#         self.meal = Meal.objects.create(
#             name="Pasta",
#             created_by=self.user,  # bu yerda created_by beriladi
#             # boshqa required maydonlar bo'lsa ularni ham kiriting
#         )
#
#         self.recipe = Recipe.objects.create(
#             meal=self.meal,
#             description="Boiling pasta and adding sauce."
#         )
#
#     def test_create_recipe(self):
#         self.assertEqual(self.recipe.meal.name, "Pasta")
#         self.assertEqual(self.recipe.description, "Boiling pasta and adding sauce.")
#
#     def test_str_method(self):
#         expected_str = f"Recipe for {self.meal.name}"
#         self.assertEqual(str(self.recipe), expected_str)
