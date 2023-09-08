import os

from django.contrib import admin
from django.contrib.auth.models import Group
from django.core.management import BaseCommand

from users.models import User


admin.site.register(Group)


class Command(BaseCommand):
    def handle(self, *args, **options):
        user = User.objects.create(
            email='admin@gmail.com',
            first_name='Admin',
            last_name='Project',
            is_staff=True,
            is_superuser=True,
            is_active=True
        )

        user.set_password(os.getenv('ADMIN_PASS'))
        user.save()
