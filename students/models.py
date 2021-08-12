from django.db import models


class Student(models.Model):
    first_name = models.CharField('First_name', max_length=200)
    last_name = models.CharField('Last_name', max_length=200)
    age = models.IntegerField('Age')

    def __str__(self):
        return f'First name: {self.first_name}, ' \
               f'Last name: {self.last_name}, ' \
               f'Age: {self.age}'
