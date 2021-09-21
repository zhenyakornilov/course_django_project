from django.forms.models import model_to_dict
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, FormView, UpdateView
from django.views.generic import ListView

from .forms import TeacherForm
from .models import Teacher


class CreateTeacherView(CreateView):
    form_class = TeacherForm
    template_name = 'teachers/create_teacher_form.html'

    def form_valid(self, form):
        Teacher.objects.create(**form.cleaned_data)
        return redirect('all-teachers')


class EditTeacherView(UpdateView):
    model = Teacher
    template_name = 'teachers/teacher_edit_form.html'
    form_class = TeacherForm
    success_url = reverse_lazy('all-teachers')


class DeleteTeacherView(DeleteView):
    model = Teacher
    success_url = reverse_lazy('all-teachers')

    def get(self, *args, **kwargs):
        return self.post(*args, **kwargs)


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
