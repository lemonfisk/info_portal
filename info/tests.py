from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from string import ascii_letters
from random import choices

from info.models import Product
from info.utils import add_two_numbers
from django.conf import settings
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

class ProductsListViewTestVase(TestCase):
    fixtures = [
        'products-fixture.json'
    ]

    def test_products(self):
        response = self.client.get(reverse("info:products_list"))
        self.assertQuerySetEqual(
            qs=Product.objects.filter(archived=False).all(),
            values=(p.pk for p in response.context["products"]),
            transform=lambda p: p.pk,
        )
        self.assertTemplateUsed(response, "info:product-list.html")


class OrdersListViewTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.user = User.objects.create_user(username="bob_test", password="qwerty")
        # cls.credentials = dict(username="bob_test", password="qwerty")
        # cls.user = User.objects.create_user(**cls.credentials)

    @classmethod
    def tearDownClass(cls):
        cls.user.delete()

    def setUp(self) -> None:
        # self.client.login(**self.credentials)
        self.client.force_login(self.user)

    def test_orders_view(self):
        response = self.client.get(reverse("info:orders_list"))
        self.assertContains(response, "Orders")

    def test_orders_view_not_authenticated(self):
        self.client.logout()
        response = self.client.get(reverse("info:orders_list"))
        self.assertEquals(response.status_code, 302)
        self.assertIn(str(settings.LOGIN_URL), response.url)
