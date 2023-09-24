from django.core.management import BaseCommand
from info.models import Product

class Command(BaseCommand):
    """
    Creates products
    """
    def handle(self, *args, **options):
        self.stdout.write("Create products")
        product_names = [
            "laptop",
            "Desc",
            "Smartphone"
        ]
        for product_name in product_names:
            product, created = Product.objects.get_or_create(name=product_name)
            self.stdout.write(f"Created product {product_name}")
        product.save()
        self.stdout.write(self.style.SUCCESS("products created"))
