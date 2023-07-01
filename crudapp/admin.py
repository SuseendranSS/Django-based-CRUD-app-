from django.contrib import admin
from crudapp.models import Student
# Register your models here.


class studentadmin(admin.ModelAdmin):
    list = ['sno', 'sname', 'sclass', 'saddr']


admin.site.register(Student, studentadmin)
