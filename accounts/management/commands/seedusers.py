from django.core.management.base import BaseCommand
from ...models import CustomUser

class Command(BaseCommand):
    help = 'Seeds the database with initial user data'

    def handle(self, *args, **kwargs):
        if not CustomUser.objects.exists():
            CustomUser.objects.create_user(username='admin', password='admin123', email='admin@example.com')
            self.stdout.write(self.style.SUCCESS('Successfully seeded users'))
        else:
            self.stdout.write(self.style.WARNING('Users already exist, no seeding performed'))