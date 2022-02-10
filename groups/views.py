from django.shortcuts import render, get_object_or_404
# Create your views here.
from django.views.generic import UpdateView

from groups.forms import GroupUpdateForm
from groups.models import Group


def get_group(request, id):
    group = get_object_or_404(Group, id=id)
    return render(
        request,
        'groups/group.html',
        {
            'group': group
        }
    )


class GroupEditView(UpdateView):
    model = Group
    form_class = GroupUpdateForm
    template_name = 'groups/edit_group.html'

    pk_url_kwarg = 'id'
