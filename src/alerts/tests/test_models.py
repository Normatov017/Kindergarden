# from django.test import TestCase
# from alerts.models import Alerts
# from products.models import Product
#
# class AlertsModelTest(TestCase):
#     def setUp(self):
#         self.product = Product.objects.create(
#             name="Test Product",
#             description="Test description",
#             price=100.00,
#             stock=10
#         )
#
#     def test_create_alert(self):
#         alert = Alerts.objects.create(
#             alert_type='LOW_STOCK',
#             product=self.product,
#             message='Stock is below threshold.'
#         )
#         self.assertEqual(alert.alert_type, 'LOW_STOCK')
#         self.assertEqual(alert.product, self.product)
#         self.assertEqual(alert.message, 'Stock is below threshold.')
#         self.assertIsNotNone(alert.created_at)
#
#     def test_alert_str_method(self):
#         alert = Alerts.objects.create(
#             alert_type='EXPIRY_SOON',
#             product=self.product,
#             message='This product will expire soon.'
#         )
#         expected_str = f"{alert.alert_type} - {self.product}"
#         self.assertEqual(str(alert), expected_str)
#
#     def test_alert_type_choices(self):
#         alert = Alerts.objects.create(
#             alert_type='GENERAL',
#             product=self.product,
#             message='This is a general alert.'
#         )
#         self.assertIn(alert.alert_type, dict(Alerts.ALERT_TYPES))
