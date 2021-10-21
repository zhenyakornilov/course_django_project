from django.db import models


class Teacher(models.Model):
    subject = models.CharField('Subject', max_length=200, db_column='Subject')
    first_name = models.CharField('First name', max_length=200, db_column='First name')
    last_name = models.CharField('Last name', max_length=200, db_column='Last name')
    age = models.IntegerField('Age', db_column='Age')

    class Meta:
        ordering = ['id']

    def __str__(self):
        return f'ID: {self.id}, '\
               f'Subject: {self.subject}, ' \
               f'First name: {self.first_name}, ' \
               f'Last name: {self.last_name}, ' \
               f'Age: {self.age}'
