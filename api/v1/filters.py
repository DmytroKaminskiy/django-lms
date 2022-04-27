import django_filters
from students.models import Student


class StudentFilter(django_filters.FilterSet):
    class Meta:
        model = Student
        fields = {
            'age': ['gte', 'lte', 'exact'],  # ?age__gte=20&age__lte=50&age__exact=35
            'first_name': ['icontains'],
        }

# filter(age__gte=20)
# filter(age__lte=20)
# filter(age=20)