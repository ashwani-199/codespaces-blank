from django.shortcuts import render, redirect
from . models import Employee, Department, Role
from . form import EmployeeForm, RoleForm, DepartmentForm
from django.db.models import Q
from django.contrib import messages


def all_emp(request):
    employee = Employee.objects.all()

    if request.method == 'GET':
        name = request.GET.get('name')
        if name != None:
            employee = Employee.objects.filter(first_name__icontains=name)



    context = {
        'employee': employee
    }

    return render(request, 'index.html', context)

def add_dept(request):
    if request.method == 'POST':
        form = RoleForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            location = form.cleaned_data['location']
            

            department = Department()
            department.name = name
            department.location = location
            
            department.save()
            messages.success(request, "Department added successfully")
    else:
        form = DepartmentForm()

    context = {
        'form': form
    }
    return render(request, 'dept.html', context)

def add_role(request):
    if request.method == 'POST':
        form = RoleForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            

            role = Role()
            role.name = name
            
            role.save()
            messages.success(request, "Role added successfully")
    else:
        form = RoleForm()

    context = {
        'form': form
    }
    return render(request, 'role.html', context)

def add_emp(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            dept = form.cleaned_data['dept']
            salary = form.cleaned_data['salary']
            bones = form.cleaned_data['bones']
            role = form.cleaned_data['role']
            phone = form.cleaned_data['phone']

            employee = Employee()
            employee.first_name = first_name
            employee.last_name = last_name
            employee.dept = dept
            employee.salary = salary
            employee.bones = bones
            employee.role = role
            employee.phone = phone

            employee.save()
            messages.success(request, "Employee added successfully")
            # return HttpResponse('Employee added successfully')
    else:
        form = EmployeeForm()

    context = {
        'form': form
    }
    return render(request, 'add.html', context)


def remove_emp(request, id):
    employee = Employee.objects.get(id=id)
    if not employee:
        return redirect('enroll.all_emp')
    employee.delete()
    messages.success(request, "Employee deleted successfully")
    return render(request, 'view.html')