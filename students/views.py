from django.forms.models import model_to_dict
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse

from faker import Faker

from .forms import StudentForm
from .models import Student

fake = Faker()


def main_page(request):
    return HttpResponse('<h1>Python course homework №4</h1>')


def create_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            Student.objects.create(**form.cleaned_data)
            return HttpResponseRedirect(reverse('all-students'))
    else:
        form = StudentForm()

    return render(request, 'students/create_student_form.html', {'form': form})

    # previous version of function 'generate_student'
    # student = Student.objects.create(first_name=fake.first_name(),
    #                                  last_name=fake.last_name(),
    #                                  age=fake.random_int(18, 26))
    # result_dict = {student.id: {'ID': student.id,
    #                             'First name': student.first_name,
    #                             'Last name': student.last_name,
    #                             'Age': student.age}}
    #
    # return JsonResponse(result_dict)


def generate_students(request):
    count = request.GET.get('count', '0')
    if count.isnumeric() and 0 < int(count) <= 100:
        result_dict = {}
        for i in range(1, int(count) + 1):
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


def edit_student(request, student_id):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            Student.objects.update_or_create(defaults=form.cleaned_data, id=student_id)
            return HttpResponseRedirect(reverse('all-students'))
    else:
        student = Student.objects.filter(id=student_id).first()
        form = StudentForm(model_to_dict(student))

    return render(request, 'students/student_edit_form.html', {'form': form, 'student_id': student_id})


def delete_student(request, student_id):
    Student.objects.filter(id=student_id).delete()
    return HttpResponseRedirect(reverse('all-students'))


def show_all_students(request):
    filter_params = {}
    student_id = request.GET.get('id', '')
    if student_id:
        filter_params['id'] = teacher_id

    student_first_name = request.GET.get('first_name', '')
    if student_first_name:
        filter_params['first_name'] = student_first_name

    student_last_name = request.GET.get('last_name', '')
    if student_last_name:
        filter_params['last_name'] = student_last_name

    student_age = request.GET.get('age', '')
    if student_age:
        filter_params['age'] = student_age

    students_list = Student.objects.filter(**filter_params)
    return render(request, 'students/students_list.html', {'students': students_list})

    # previous version of function
    # students = Student.objects.all()
    # result_dict = {}
    # for student in students:
    #     counter = student.id
    #     inside_dict = {'ID': student.id,
    #                    'First name': student.first_name,
    #                    'Last name': student.last_name,
    #                    'Age': student.age}
    #     result_dict.update({counter: inside_dict})
    #
    # return JsonResponse(result_dict)
