from django.core.management import BaseCommand
from django.contrib.auth.models import User
from info.models import Order


class Command(BaseCommand):

    def handle(self, *args, **options):
        self.stdout.write("Create oreder")
        user = User.objects.get(username="mdi")
        order = Order.objects.get_or_create(
            delivery_address="HHHHHHHH",
            promocode="Sale123",
            user=user
        )
        self.stdout.write(f"Created order {order}")
