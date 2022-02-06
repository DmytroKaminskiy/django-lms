from django.shortcuts import render, get_object_or_404

# Create your views here.
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
