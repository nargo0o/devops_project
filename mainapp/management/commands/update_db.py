from django.core.management.base import BaseCommand
from mainapp.models import ProductCategory, Product
from authapp.models import ShopUser

from authapp.models import ShopUserProfile


class Command(BaseCommand):
    help = 'Update DB'

    def handle(self, *args, **options):
        users = ShopUser.objects.all()
        for user in users:
            users_profile = ShopUserProfile.objects.create(user=user)
            users_profile.save()

