import os

from django.core.management.base import BaseCommand
from django.contrib.auth.models import User


class Command(BaseCommand):
    """Performs initial setup."""
    def handle(self, *args, **kwargs):
        username = os.environ['SUPERUSER_NAME']
        password = os.environ['SUPERUSER_PASSWORD']
        email = os.environ['SUPERUSER_EMAIL']

        defaults = {
            'email': email,
            'is_superuser': True,
            'is_staff': True,
        }

        superuser, created = User.objects.update_or_create(
            username=username,
            defaults=defaults,
        )

        superuser.set_password(password)

        if created:
            superuser.save()
            self.stdout.write('Successfully created superuser %s.' % username)
        else:
            self.stdout.write('Superuser %s updated.' % username)
