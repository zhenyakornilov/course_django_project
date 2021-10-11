import factory

from faker import Faker

from students.models import Logger, Student

fake = Faker()


class StudentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Student

    first_name = fake.first_name()
    last_name = fake.last_name()
    age = fake.random_int(18, 26)
    phone_number = '380668008080'


class LoggerFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Logger

    method = 'GET'
    path = '/admin/'
    execution_time = 0.1
