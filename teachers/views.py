from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

from .forms import TeacherForm
from .models import Teacher


def generate_teacher(request):
    if request.method == 'POST':
        form = TeacherForm(request.POST)

        if form.is_valid():
            Teacher.objects.create(**form.cleaned_data)
            return HttpResponse('Teacher created!')

    elif request.method == 'GET':
        form = TeacherForm()

    return render(request, 'teachers/generate_teacher.html', {'form': form})


def show_all_teachers(request):
    filter_params = {}

    teacher_first_name = request.GET.get('first_name', '')
    if teacher_first_name:
        filter_params['first_name'] = teacher_first_name

    teacher_last_name = request.GET.get('last_name', '')
    if teacher_last_name:
        filter_params['last_name'] = teacher_last_name

    teacher_age = request.GET.get('age', '')
    if teacher_age:
        filter_params['age'] = teacher_age

    teachers = Teacher.objects.filter(**filter_params)
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
