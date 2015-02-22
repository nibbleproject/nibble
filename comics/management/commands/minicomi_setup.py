import os

from django.core.management.base import BaseCommand
from django.contrib.auth.models import User


class Command(BaseCommand):
    """Performs initial setup."""
    def handle(self, *args, **kwargs):
        username = os.environ['SUPERUSER_NAME']
        password = os.environ['SUPERUSER_PASSWORD']

        superuser, created = User.objects.get_or_create(
            username=username,
            is_superuser=True,
            is_staff=True,
        )

        if created:
            superuser.set_password(password)
            superuser.save()

            self.stdout.write('Successfully created superuser %s.' % username)
        else:
            self.stdout.write('Superuser %s already exists.' % username)
