from django.contrib import admin

# Register your models here.
from students.models import Student, Lecture


class StudentAdmin(admin.ModelAdmin):
    list_per_page = 10
    list_display = ['id', 'name', 'email', 'age']
    search_fields = ['first_name', 'last_name']
    list_filter = ['group__name']


admin.site.register(Student, StudentAdmin)
admin.site.register(Lecture)
