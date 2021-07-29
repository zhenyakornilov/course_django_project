from django.http import JsonResponse
from .models import Teacher


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

