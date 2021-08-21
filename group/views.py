from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

from . forms import GroupForm
from .models import Group


def create_group(request):
    if request.method == 'POST':
        form = GroupForm(request.POST)

        if form.is_valid():
            Group.objects.create(**form.cleaned_data)
            return HttpResponse('Group created!')

    elif request.method == 'GET':
        form = GroupForm()

    return render(request, 'group/create_group.html', {'form': form})


def show_all_groups(request):
    groups = Group.objects.all()
    result_dict = {}
    for group in groups:
        counter = group.id
        inside_dict = {'Group name': group.group_name,
                       'Count of students': group.students_in_group}
        result_dict.update({counter: inside_dict})

    return JsonResponse(result_dict)
