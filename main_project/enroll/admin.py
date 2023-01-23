from django.contrib import admin
from . models import Role, Department, Employee


# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'dept', 'role', 'salary', 'bones', 'phone', 'hire_date']

admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Department)
admin.site.register(Role)
