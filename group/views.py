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
    filter_params = {}
    group_id = request.GET.get('id', '')
    if group_id:
        filter_params['id'] = group_id

    group_name = request.GET.get('group_name', '')
    if group_name:
        filter_params['group_name'] = group_name

    group_list = Group.objects.filter(**filter_params)
    return render(request, 'group/group_list.html', {'groups': group_list})
