from django.test import TestCase
from django.urls import reverse
from string import ascii_letters
from random import choices

from info.models import Product
from info.utils import add_two_numbers
# Create your tests here.

class AddTwoNumbersTestCase(TestCase):
    def test_add_two_numbers(self):
        result = add_two_numbers(2, 5)
        self.assertEquals(result, 7)

class ProductCreateViewTestCase(TestCase):
    def setUp(self) -> None:
        self.product_name = "".join(choices(ascii_letters, k=10))
        Product.objects.filter(name=self.product_name).delete()
    def test_create_product(self):
        response = self.client.post(
            reverse("info:product_create"),
            {
                "name": self.product_name,
                "price": "123,45",
                "description": "A good table",
                "discount": "10",
            }
        )
        self.assertRedirects(response, reverse("info:products_list"))
        self.assertTrue(
            Product.objects.filter(name=self.product_name).exists()
        )

class ProductDetailsViewTestCase(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.product = Product.objects.create(name="Best products")

    @classmethod
    def tearDown(cls) -> None:
        cls.product.delete()

    # def setUp(self) -> None:
    #     self.product = Product.objects.create(name="Best products")

    # def tearDown(self) -> None:
    #     self.product.delete()

    def test_get_product(self):
        response = self.client.get(
            reverse("info:product_details", kwargs={"pk": self.product.pk})
        )
        self.assertEqual(response.status_code, 200)

    def test_get_product_and_check_content(self):
        response = self.client.get(
            reverse("info:product_details", kwargs={"pk": self.product.pk})
        )
        self.assertContains(response, self.product.name)