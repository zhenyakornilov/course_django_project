import factory

from faker import Faker

from teachers.models import Teacher

fake = Faker()

teacher_subjects = ['Math', 'Physics', 'Chemistry', 'History',
                    'Music', 'Spanish', 'English', 'Computing', 'Geography']


class TeacherFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Teacher

    subject = teacher_subjects[fake.random_int(0, 8)]
    first_name = fake.first_name()
    last_name = fake.last_name()
    age = fake.random_int(30, 60)
