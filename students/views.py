# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt

from students.forms import StudentCreateForm, StudentUpdateForm
from students.models import Student
from students.utils import render_students_list_html


def get_students(request):
    qs = Student.objects.all()
    params = [
        'first_name',
        'first_name__startswith',
        'first_name__endswith',
        'first_name__contains',
        'last_name',
        'age',
        'age__gt',
        'age__lt',
    ]

    query = {}

    form = f"""<form>
        <p>Search students</p>
        <p>
            <input type="text" name="first_name"
                value="{request.GET.get('first_name', '')}"
                placeholder="Input First Name">
        </p>
        <p>
            <input type="text" name="last_name"
                value="{request.GET.get('last_name', '')}"
                placeholder="Input Last Name">
        </p>
        <p>
            <input type="number" name="age"
                value="{request.GET.get('age', '')}"
                placeholder="Input Age">
        </p>
        <p><button type="submit">Search</button></p>
    </form>
    <br>
    <a href="/students/create">Add new student</a><br>
    """

    for param_name in params:
        param_value = request.GET.get(param_name)
        if param_value:
            if ',' in param_value and '__' not in param_name:
                param_values = param_value.split(',')
                query[param_name + '__in'] = param_values
            else:
                query[param_name] = param_value

    try:
        qs = qs.filter(**query)
    except ValueError as e:
        return HttpResponse(f"Error wrong input data. {str(e)}", status=400)

    qs = qs.order_by('-id')
    return render_students_list_html(qs[:20], form)


@csrf_exempt
def create_student(request):
    if request.method == 'POST':
        form = StudentCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/students/')
    else:
        form = StudentCreateForm()

    html = f"""
        <form method="post">
            {form.as_p()}
            <p><button type="submit">Create Student</button></p>
        </form>
    """

    return HttpResponse(html)


@csrf_exempt
def update_student(request, id):
    student = Student.objects.get(id=id)

    if request.method == 'POST':
        form = StudentUpdateForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/students/')
    else:
        form = StudentUpdateForm(instance=student)

    html = f"""
        <form method="post">
            {form.as_p()}
            <p><button type="submit">Update Student</button></p>
        </form>
    """

    return HttpResponse(html)
