from django.core.management.base import BaseCommand, CommandError
from teachers.models import Teacher
from random import randint

from faker import Faker

teacher_subjects = ['Math', 'Physics', 'Chemistry', 'History',
                    'Music', 'Spanish', 'English', 'Computing', 'Geography']


class Command(BaseCommand):
    help = 'This command generates teachers for a given number'

    def add_arguments(self, parser):
        parser.add_argument('number_of_teachers', nargs='?', type=int, default=100)

    def handle(self, *args, **options):
        fake = Faker()

        for i in range(options['number_of_teachers']):
            teacher_obj = Teacher.objects.create(subject=teacher_subjects[randint(0, 8)],
                                                 first_name=fake.first_name(),
                                                 last_name=fake.last_name(),
                                                 age=fake.random_int(27, 60))

        self.stdout.write(self.style.SUCCESS(f"Successfully created {options['number_of_teachers']} teachers"))
