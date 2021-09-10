from django.core.management.base import BaseCommand

from faker import Faker

from teachers.models import Teacher

from students.models import Student

from group.models import Group

teacher_subjects = ['Math', 'Physics', 'Chemistry', 'History',
                    'Music', 'Spanish', 'English', 'Computing', 'Geography']


class Command(BaseCommand):
    help = 'This command generates teachers for a given number'

    def add_arguments(self, parser):
        parser.add_argument('number_of_teachers', nargs='?', type=int, default=100)

    def handle(self, *args, **options):
        fake = Faker()
        result = []
        for i in range(options['number_of_teachers']):
            teacher = Teacher(subject=teacher_subjects[fake.random_int(0, 8)],
                              first_name=fake.first_name(),
                              last_name=fake.last_name(),
                              age=fake.random_int(27, 60))
            teacher.save()

            for student in range(fake.random_int(0, 11)):
                student = Student(first_name=fake.first_name(),
                                  last_name=fake.last_name(),
                                  age=fake.random_int(18, 26))
                result.append(student)
            Student.objects.bulk_create(result)

            group = Group(group_name=teacher_subjects[fake.random_int(0, 8)],
                          group_curator=teacher,
                          group_monitor=Student.objects.last(),
                          students_in_group=len(result))
            group.save()

        self.stdout.write(self.style.SUCCESS(f"Successfully created {options['number_of_teachers']} teacher(s)"))
