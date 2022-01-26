# Create your views here.
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

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

    qs = qs.order_by('-id')

    students_filter = StudentFilter(data=request.GET, queryset=qs)

    return render(request, 'list_students.html', {
        'args': request.GET,
        'filter': students_filter
    })


@csrf_exempt
def create_student(request):
    if request.method == 'POST':
        form = StudentCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('list_students'))
    else:
        form = StudentCreateForm()

    return render(request, 'create_student.html', {
        'form': form
    })


@csrf_exempt
def update_student(request, id):
    student = get_object_or_404(Student, id=id)

    if request.method == 'POST':
        form = StudentUpdateForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('list_students'))
    else:
        form = StudentUpdateForm(instance=student)

    return render(request, 'edit_student.html', {
        'form': form
    })
