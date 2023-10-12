from django.test import TestCase
from info.utils import add_two_numbers
# Create your tests here.

class AddTwoNumbersTestCase(TestCase):
    def test_add_two_numbers(self):
        result = add_two_numbers(2, 5)
        self.assertEquals(result, 7)