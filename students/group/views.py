from django.http import JsonResponse
from .models import Group


def show_all_groups(request):
    groups = Group.objects.all()
    result_dict = {}
    for group in groups:
        counter = group.id
        inside_dict = {'Group name': group.group_name,
                       'Count of students': group.students_in_group}
        result_dict.update({counter: inside_dict})

    return JsonResponse(result_dict)


