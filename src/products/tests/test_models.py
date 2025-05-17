from django.test import TestCase
from products.models import Product

class ProductModelTest(TestCase):

    def test_create_product(self):
        product = Product.objects.create(
            name="Sugar",
            unit="kg",
            minimum_threshold=5.00
        )
        self.assertEqual(product.name, "Sugar")
        self.assertEqual(product.unit, "kg")
        self.assertEqual(product.minimum_threshold, 5.00)
        self.assertIsNotNone(product.created_at)

    def test_str_method(self):
        product = Product.objects.create(
            name="Salt",
            unit="kg",
            minimum_threshold=2.00
        )
        self.assertEqual(str(product), "Salt")
