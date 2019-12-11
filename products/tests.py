from django.test import TestCase
from .models import Product

# Create your tests here.
class ProductTests(TestCase):
    """Here we'll define the tests that we will run agains our product models"""

    def test_str(self):
        test_name = Product(name = 'A Product')
        self.assertEqual(str(test_name), 'A Product')