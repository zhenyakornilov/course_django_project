from django.http import JsonResponse
from .models import Teacher
from faker import Faker
from random import randint

teacher_subjects = ['Math', 'Physics', 'Chemistry', 'History',
                    'Music', 'Spanish', 'English', 'Computing', 'Geography']


def show_all_teachers(request):
    teachers = Teacher.objects.all()
    result_dict = {}
    for teacher in teachers:
        counter = teacher.id
        inside_dict = {'ID': teacher.id,
                       'Subject': teacher.subject,
                       'First name': teacher.first_name,
                       'Last name': teacher.last_name,
                       'Age': teacher.age}
        result_dict.update({counter: inside_dict})

    return JsonResponse(result_dict)


def generate_teachers(request):
    fake = Faker()
    count = request.GET.get('count', '100')
    if count.isnumeric() and 0 < int(count) <= 100:
        result_dict = {}
        for i in range(1, int(count)+1):
            teacher_obj = Teacher.objects.create(subject=teacher_subjects[randint(0, 8)],
                                                 first_name=fake.first_name(),
                                                 last_name=fake.last_name(),
                                                 age=fake.random_int(27, 60))
            counter = teacher_obj.id
            inside_dict = {'ID': teacher_obj.id,
                           'Subject': teacher_obj.subject,
                           'First name': teacher_obj.first_name,
                           'Last name': teacher_obj.last_name,
                           'Age:': teacher_obj.age}
            result_dict.update({counter: inside_dict})

        return JsonResponse(result_dict)
