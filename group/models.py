from django.db import models


class Group(models.Model):
    group_name = models.CharField('Group Name', max_length=200)
    students_in_group = models.IntegerField('Students in group')

    def __str__(self):
        return self.group_name
