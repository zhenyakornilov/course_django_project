from django.forms.models import model_to_dict
from django.shortcuts import redirect, render

from .forms import TeacherForm
from .models import Teacher

from django.views.generic import ListView


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


class TeachersListView(ListView):
    model = Teacher
    template_name = 'teachers/teachers_list.html'

    def get_queryset(self):
        filter_params = {}
        teacher_id = self.request.GET.get('id', '')
        if teacher_id:
            filter_params['id'] = teacher_id
        teacher_first_name = self.request.GET.get('first_name', '')
        if teacher_first_name:
            filter_params['first_name'] = teacher_first_name
        teacher_last_name = self.request.GET.get('last_name', '')
        if teacher_last_name:
            filter_params['last_name'] = teacher_last_name
        teacher_age = self.request.GET.get('age', '')
        if teacher_age:
            filter_params['age'] = teacher_age
        queryset = Teacher.objects.filter(**filter_params)
        return queryset
