from django.urls import path

from students.views import get_students, StudentEditView, StudentDeleteView, \
    StudentCreateView

app_name = 'students'

urlpatterns = [
    path('', get_students, name='list_students'),
    path('create', StudentCreateView.as_view(), name='create_students'),
    path('update/<int:id>', StudentEditView.as_view(),
         name='update_students'),
    path('delete/<int:id>', StudentDeleteView.as_view(),
         name='delete_students'),
]
