import factory

from faker import Faker

from students.models import Student

fake = Faker()


class StudentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Student

    first_name = fake.first_name()
    last_name = fake.last_name()
    age = fake.random_int(18, 26)
    phone_number = '380668008080'
