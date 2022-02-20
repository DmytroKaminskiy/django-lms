# Create your views here.
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic import UpdateView, DeleteView, CreateView, ListView

from students.forms import StudentCreateForm, StudentUpdateForm, StudentFilter
from students.models import Student


class StudentListView(ListView):
    model = Student
    template_name = 'students/list_students.html'
    paginate_by = 5

    def get_filter(self, queryset=None):
        if not queryset:
            queryset = self.get_queryset()
        return StudentFilter(data=self.request.GET, queryset=queryset)

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.select_related('group__headman').order_by('-id')
        filter_ = self.get_filter(queryset)
        return filter_.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = self.get_filter()

        # paginator = Paginator(self.get_queryset(), 5)
        # page_number = self.request.GET.get('page', '1')
        # page_obj = paginator.page(int(page_number))
        # context['page_obj'] = page_obj

        return context


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
