# Create your views here.
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import UpdateView, DeleteView, CreateView

from students.forms import StudentCreateForm, StudentUpdateForm, StudentFilter
from students.models import Student


def get_students(request):
    qs = Student.objects.all()

    qs = qs.select_related('group__headman').order_by('-id')

    students_filter = StudentFilter(data=request.GET, queryset=qs)

    return render(request, 'students/list_students.html', {
        'filter': students_filter
    })


class StudentCreateView(CreateView):
    model = Student
    success_url = reverse_lazy('students:list_students')
    form_class = StudentCreateForm
    template_name = 'students/create_student.html'


class StudentEditView(UpdateView):
    model = Student
    success_url = reverse_lazy('students:list_students')
    form_class = StudentUpdateForm
    template_name = 'students/edit_student.html'
    pk_url_kwarg = 'id'


class StudentDeleteView(DeleteView):
    model = Student
    pk_url_kwarg = 'id'
    template_name = 'students/delete_student.html'
    success_url = reverse_lazy('students:list_students')


# Not used
def delete_student_no_confirmation(request, id):
    try:
        student = Student.objects.get(id=id)
        student.delete()
    except Student.DoesNotExist:
        pass
    return HttpResponseRedirect(reverse('students:list_students'))
