from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.views.generic import ListView
from django.views.generic.edit import CreateView

from . forms import GroupForm
from .models import Group


class CreateGroupView(LoginRequiredMixin, CreateView):
    form_class = GroupForm
    template_name = 'group/create_group.html'

    def form_valid(self, form):
        Group.objects.create(**form.cleaned_data)
        return redirect('all-groups')


class GroupListView(ListView):
    model = Group
    template_name = 'group/group_list.html'
    paginate_by = 20

    def get_queryset(self):
        filter_params = {}
        group_id = self.request.GET.get('id', '')
        if group_id:
            filter_params['id'] = group_id

        group_name = self.request.GET.get('group_name', '')
        if group_name:
            filter_params['group_name'] = group_name

        queryset = Group.objects.filter(**filter_params)
        return queryset
