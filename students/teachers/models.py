from django.db import models


class Teacher(models.Model):
    subject = models.CharField('Subject', max_length=200)
    first_name = models.CharField('First name', max_length=200)
    last_name = models.CharField('Last name', max_length=200)
    age = models.IntegerField('Age')

    def __str__(self):
        return f'Subject: {self.subject}, ' \
               f'First name: {self.first_name}, ' \
               f'Last name: {self.last_name}, ' \
               f'Age: {self.age}'

