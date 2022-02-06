# Create your views here.
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from students.forms import StudentCreateForm, StudentUpdateForm, StudentFilter
from students.models import Student


def get_students(request):
    qs = Student.objects.all()
    # params = [
    #     'first_name',
    #     'first_name__startswith',
    #     'first_name__endswith',
    #     'first_name__contains',
    #     'last_name',
    #     'age',
    #     'age__gt',
    #     'age__lt',
    # ]
    #
    # query = {}
    #
    # for param_name in params:
    #     param_value = request.GET.get(param_name)
    #     if param_value:
    #         if ',' in param_value and '__' not in param_name:
    #             param_values = param_value.split(',')
    #             query[param_name + '__in'] = param_values
    #         else:
    #             query[param_name] = param_value
    #
    # try:
    #     qs = qs.filter(**query)
    # except ValueError as e:
    #     return HttpResponse(f"Error wrong input data. {str(e)}", status=400)

    qs = qs.select_related('group__headman').order_by('-id')

    students_filter = StudentFilter(data=request.GET, queryset=qs)

    return render(request, 'students/list_students.html', {
        'filter': students_filter
    })


def create_student(request):
    if request.method == 'POST':
        form = StudentCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('students:list_students'))
    else:
        form = StudentCreateForm()

    return render(request, 'students/create_student.html', {
        'form': form
    })


def update_student(request, id):
    student = get_object_or_404(Student, id=id)

    if request.method == 'POST':
        form = StudentUpdateForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('students:list_students'))
    else:
        form = StudentUpdateForm(instance=student)

    return render(request, 'students/edit_student.html', {
        'form': form
    })


def delete_student(request, id):
    student = get_object_or_404(Student, id=id)

    if request.method == 'POST':
        student.delete()
        return HttpResponseRedirect(reverse('students:list_students'))

    return render(
        request,
        'students/delete_student.html',
        {
            'student': student
        }
    )


# Not used
def delete_student_no_confirmation(request, id):
    try:
        student = Student.objects.get(id=id)
        student.delete()
    except Student.DoesNotExist:
        pass
    return HttpResponseRedirect(reverse('students:list_students'))
