from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
import getpass

class Command(BaseCommand):
    help = 'Create a superuser with external_id'

    def handle(self, *args, **options):
        User = get_user_model()

        username = input('Username: ')
        email = input('Email: ')
        external_id = input('External ID: ')
        password = getpass.getpass('Password: ')
        password_confirm = getpass.getpass('Password (again): ')

        if password != password_confirm:
            self.stderr.write("Error: Your passwords didn't match.")
            return

        if not User.objects.filter(username=username).exists():
            User.objects.create_superuser(username=username, email=email, external_id=external_id, password=password)
            self.stdout.write(self.style.SUCCESS('Superuser created successfully'))
        else:
            self.stdout.write(self.style.ERROR('Superuser already exists'))
