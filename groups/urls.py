from django.urls import path

from groups.views import get_group

app_name = 'groups'

urlpatterns = [
    path('<int:id>', get_group, name='group'),
]
