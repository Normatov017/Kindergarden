# from django.test import TestCase
# from datetime import date
# from products.models import Product
# from users.models import user
# from inventory.models import Inventory
#
# class InventoryModelTest(TestCase):
#     def setUp(self):
#         # Product model uchun to'g'ri maydonlar bilan yaratish
#         self.product = Product.objects.create(
#             name="Milk",
#             unit="liter",
#             minimum_threshold=5.00
#         )
#
#         # User model uchun minimal kerakli maydonlar
#         self.test_user = user.objects.create(
#             username="testuser",
#             email="test@example.com",
#             password="testpass"
#         )
#
#         self.inventory = Inventory.objects.create(
#             product=self.product,
#             quantity=15.00,
#             delivery_date=date.today(),
#             expiry_date=date.today(),
#             source="Local supplier",
#             created_by=self.test_user
#         )
#
#     def test_create_inventory(self):
#         self.assertEqual(self.inventory.product.name, "Milk")
#         self.assertEqual(float(self.inventory.quantity), 15.00)
#         self.assertEqual(self.inventory.source, "Local supplier")
#         self.assertEqual(self.inventory.created_by.username, "testuser")
#
#     def test_str_method(self):
#         expected_str = f"{self.product.name} - {self.inventory.quantity:.2f}"
#         actual_str = str(self.inventory)
#         self.assertEqual(actual_str, expected_str)
