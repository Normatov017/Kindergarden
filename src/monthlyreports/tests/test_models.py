from django.test import TestCase
from monthlyreports.models import MonthlyReports
from decimal import Decimal
from datetime import datetime

class MonthlyReportsModelTest(TestCase):

    def setUp(self):
        self.report = MonthlyReports.objects.create(
            month_year="2025-05",
            total_served=150,
            total_possible=200,
            difference_percent=Decimal('25.00')
        )

    def test_report_creation(self):
        """Test that a MonthlyReports object is created correctly"""
        self.assertEqual(self.report.month_year, "2025-05")
        self.assertEqual(self.report.total_served, 150)
        self.assertEqual(self.report.total_possible, 200)
        self.assertEqual(self.report.difference_percent, Decimal('25.00'))
        self.assertIsNotNone(self.report.generated_at)

    def test_str_method(self):
        """Test the string representation of the MonthlyReports object"""
        self.assertEqual(str(self.report), "Report for 2025-05")
