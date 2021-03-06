import django_filters
from django.core.exceptions import ValidationError
from django.forms import ModelForm

from students.models import Student


class StudentFilter(django_filters.FilterSet):
    class Meta:
        model = Student
        fields = {
            'first_name': ['iexact'],
            'last_name': ['iexact'],
            'age': ['exact'],
        }


class StudentBaseForm(ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

    def clean(self):
        result = super().clean()
        if not self.errors:
            enroll_date = self.cleaned_data['enroll_date']
            graduate_date = self.cleaned_data['graduate_date']

            if enroll_date > graduate_date:
                raise ValidationError("Enroll date cannot be less "
                                      "than gradate date")

        return result

    def clean_phone_number(self):
        phone_number = self.cleaned_data['phone_number']

        has_phone_number_qs = Student.objects.filter(
            phone_number=phone_number
        )

        if self.instance:
            has_phone_number_qs = has_phone_number_qs.exclude(
                id=self.instance.id
            )

        if has_phone_number_qs.exists():
            raise ValidationError("Phone number is not unique")

        return phone_number


class StudentCreateForm(StudentBaseForm):
    pass


class StudentUpdateForm(StudentBaseForm):
    class Meta:
        model = Student
        exclude = ['age']
