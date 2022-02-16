from django.contrib import admin

from groups.models import Group
from students.models import Student


class StudentTable(admin.TabularInline):
    model = Student
    fields = ['first_name', 'last_name']
    readonly_fields = fields
    show_change_link = True


class GroupAdmin(admin.ModelAdmin):
    list_per_page = 10
    list_display = ['id', 'name']
    inlines = [StudentTable]
    list_editable = ('name',)
    autocomplete_fields = ('headman', )


admin.site.register(Group, GroupAdmin)
