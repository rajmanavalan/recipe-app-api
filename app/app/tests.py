from django.test import TestCase

from app.calc import add, substract

class CalcTests(TestCase):
    def test_add_numbers(self):
        """Test that tow numbers are added together"""
        self.assertEqual(add(3,8),11)
    
    def test_substract_numbers(self):
        """Test that tow numbers are added together"""
        self.assertEqual(substract(3,8),5)