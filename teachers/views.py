from django.forms.models import model_to_dict
from django.shortcuts import redirect, render

from .forms import TeacherForm
from .models import Teacher


def create_teacher(request):
    if request.method == 'POST':
        form = TeacherForm(request.POST)
        if form.is_valid():
            Teacher.objects.create(**form.cleaned_data)
            return redirect('all-teachers')
    else:
        form = TeacherForm()

    return render(request, 'teachers/create_teacher_form.html', {'form': form})


def edit_teacher(request, teacher_id):
    if request.method == 'POST':
        form = TeacherForm(request.POST)
        if form.is_valid():
            Teacher.objects.update_or_create(defaults=form.cleaned_data, id=teacher_id)
            return redirect('all-teachers')
    else:
        teacher = Teacher.objects.filter(id=teacher_id).first()
        form = TeacherForm(model_to_dict(teacher))

    return render(request, 'teachers/teacher_edit_form.html', {'form': form, 'teacher_id': teacher_id})


def delete_teacher(request, teacher_id):
    Teacher.objects.filter(id=teacher_id).delete()
    return redirect('all-teachers')


def show_all_teachers(request):
    filter_params = {}
    teacher_id = request.GET.get('id', '')
    if teacher_id:
        filter_params['id'] = teacher_id

    teacher_first_name = request.GET.get('first_name', '')
    if teacher_first_name:
        filter_params['first_name'] = teacher_first_name

    teacher_last_name = request.GET.get('last_name', '')
    if teacher_last_name:
        filter_params['last_name'] = teacher_last_name

    teacher_age = request.GET.get('age', '')
    if teacher_age:
        filter_params['age'] = teacher_age

    teachers_list = Teacher.objects.filter(**filter_params)
    return render(request, 'teachers/teachers_list.html', {'teachers': teachers_list})

    # previous block of function
    # result_dict = {}
    # for teacher in teachers:
    #     counter = teacher.id
    #     inside_dict = {'ID': teacher.id,
    #                    'Subject': teacher.subject,
    #                    'First name': teacher.first_name,
    #                    'Last name': teacher.last_name,
    #                    'Age': teacher.age}
    #     result_dict.update({counter: inside_dict})
    #
    # return JsonResponse(result_dict)
