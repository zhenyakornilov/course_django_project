from django.contrib import messages
# from django.forms.models import model_to_dict
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import ListView, View
from django.views.generic.edit import CreateView, DeleteView, UpdateView


from faker import Faker

from .forms import GenerateStudentsForm, StudentForm
from .models import Student
from .tasks import generate_random_students

fake = Faker()


class MainPage(View):
    def get(self, request):
        return render(request, 'students/index.html')


class CreateStudentView(CreateView):
    form_class = StudentForm
    template_name = 'students/create_student_form.html'

    def form_valid(self, form):
        Student.objects.create(**form.cleaned_data)
        return redirect('all-students')
# def create_student(request):
#     if request.method == 'POST':
#         form = StudentForm(request.POST)
#         if form.is_valid():
#             student_obj = Student(**form.cleaned_data)
#             student_obj.save()
#             return redirect('all-students')
#     else:
#         form = StudentForm()
#
#     return render(request, 'students/create_student_form.html', {'form': form})


def generate_students(request):
    count = request.GET.get('count', '0')
    if count.isnumeric() and 0 < int(count) <= 100:
        result_dict = {}
        for i in range(1, int(count) + 1):
            student_obj = Student(first_name=fake.first_name(),
                                  last_name=fake.last_name(),
                                  age=fake.random_int(18, 26))
            student_obj.save()
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


class EditStudentView(UpdateView):
    model = Student
    template_name = 'students/student_edit_form.html'
    fields = ['first_name', 'last_name', 'age', 'phone_number']
    success_url = reverse_lazy('all-students')


# def edit_student(request, student_id):
#     if request.method == 'POST':
#         form = StudentForm(request.POST)
#         if form.is_valid():
#             Student.objects.update_or_create(defaults=form.cleaned_data, id=student_id)
#             return redirect('all-students')
#     else:
#         student = Student.objects.filter(id=student_id).first()
#         form = StudentForm(model_to_dict(student))
#
#     return render(request, 'students/student_edit_form.html', {'form': form, 'student_id': student_id})


class DeleteStudentView(DeleteView):
    model = Student
    success_url = reverse_lazy('all-students')

    def get(self, *args, **kwargs):
        return self.post(*args, **kwargs)


class StudentsListView(ListView):
    model = Student
    template_name = 'students/students_list.html'

    def get_queryset(self):
        filter_params = {}
        student_id = self.request.GET.get('id', '')
        if student_id:
            filter_params['id'] = student_id

        student_first_name = self.request.GET.get('first_name', '')
        if student_first_name:
            filter_params['first_name'] = student_first_name

        student_last_name = self.request.GET.get('last_name', '')
        if student_last_name:
            filter_params['last_name'] = student_last_name

        student_age = self.request.GET.get('age', '')
        if student_age:
            filter_params['age'] = student_age

        queryset = Student.objects.filter(**filter_params)
        return queryset


def generate_students_from_from(request):
    if request.method == 'POST':
        form = GenerateStudentsForm(request.POST)
        if form.is_valid():
            total = form.cleaned_data.get('total')
            generate_random_students.delay(total)
            messages.success(request, 'We are generating random students! Wait a moment and refresh this page.')
            return redirect('all-students')
    else:
        form = GenerateStudentsForm()

    return render(request, 'students/student_generator.html', {'form': form})
