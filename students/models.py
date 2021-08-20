from django.db import models


class Student(models.Model):
    first_name = models.CharField('First_name', max_length=200)
    last_name = models.CharField('Last_name', max_length=200)
    age = models.IntegerField('Age')
    phone_number = models.CharField(null=True, blank=True, unique=True, max_length=12)

    def __str__(self):
        return f'First name: {self.first_name}, ' \
               f'Last name: {self.last_name}, ' \
               f'Age: {self.age}, ' \
               f'Phone: {self.phone_number}'


class Logger(models.Model):
    method = models.CharField(max_length=10)
    path = models.CharField(max_length=200)
    execution_time = models.FloatField(null=False)
    created = models.DateTimeField(auto_now_add=True)
