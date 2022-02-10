from django.urls import path

from groups.views import get_group, GroupEditView

app_name = 'groups'

urlpatterns = [
    path('<int:id>', get_group, name='group'),
    path('update/<int:id>', GroupEditView.as_view(), name='edit_group'),
]
