from django.db import models


class Group(models.Model):
    group_name = models.CharField('Group Name', max_length=200, db_column='Group name')
    students_in_group = models.IntegerField('Students in group', null=True, db_column='Students in group')

    group_curator = models.OneToOneField("teachers.Teacher", null=True,
                                         on_delete=models.CASCADE, db_column='Group curator ID')
    group_monitor = models.OneToOneField("students.Student", null=True,
                                         on_delete=models.CASCADE, db_column='Group monitor ID')

    class Meta:
        ordering = ['id']

    def __str__(self):
        return f'{self.group_name}, {self.students_in_group}'
