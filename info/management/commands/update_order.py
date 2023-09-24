from django.core.management import BaseCommand
from info.models import Order, Product

class Command(BaseCommand):

    def handle(self, *args, **options):
        order = Order.objects.first()
        if not order:
            self.stdout.write(f"No order found")
            return

        products = Product.objects.all()
        for product in products:
            order.products.add(product)
        order.save()

        self.stdout.write(self.style.SUCCESS(f"product added {order.products.all()} to order {order}"))
