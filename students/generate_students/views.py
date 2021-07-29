from django.http import HttpResponse, JsonResponse
from .models import Student

from faker import Faker

fake = Faker()


def main_page(request):
    return HttpResponse('<h1>Python course homework №4</h1>')


def generate_one_student(request):
    student = Student.objects.create(first_name=fake.first_name(),
                                     last_name=fake.last_name(),
                                     age=fake.random_int(18, 26))
    result_dict = {student.id: {'ID': student.id,
                                'First name': student.first_name,
                                'Last name': student.last_name,
                                'Age': student.age}}

    return JsonResponse(result_dict)


def generate_students(request):
    count = request.GET.get('count', '0')
    if count.isnumeric() and 0 < int(count) <= 100:
        result_dict = {}
        for i in range(1, int(count)+1):
            student_obj = Student.objects.create(first_name=fake.first_name(),
                                                 last_name=fake.last_name(),
                                                 age=fake.random_int(18, 26))
            counter = student_obj.id
            inside_dict = {'ID': student_obj.id,
                           'First name': student_obj.first_name,
                           'Last name': student_obj.last_name,
                           'Age:': student_obj.age}
            result_dict.update({counter: inside_dict})

        return JsonResponse(result_dict)

    elif count == '0':
        return HttpResponse('<h1>Default value is 0</h1>'
                            '<br>Enter positive number from 1 too 100')
    else:
        return HttpResponse('<h3>Enter positive number from 1 too 100</h3>')


def show_all_students(request):
    students = Student.objects.all()
    result_dict = {}
    for student in students:
        counter = student.id
        inside_dict = {'ID': student.id,
                       'First name': student.first_name,
                       'Last name': student.last_name,
                       'Age': student.age}
        result_dict.update({counter: inside_dict})

    return JsonResponse(result_dict)
