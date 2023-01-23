from django import forms
from . models import Employee, Department, Role



class EmployeeForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First name'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last name'}))
    dept = forms.ModelChoiceField(queryset=Department.objects.all(), empty_label='Select Department', widget=forms.Select(attrs={'class': 'form-select'}))
    
    salary = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Salary'}))
    bones = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Bones'}))
    role = forms.ModelChoiceField(queryset=Role.objects.all(), empty_label='Select Role', widget=forms.Select(attrs={'class': 'form-select'}))
    
    phone = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone number'}))


    class Meta:
        model = Employee
        fields = ('first_name', 'last_name', 'dept', 'salary', 'bones', 'role', 'phone')


class RoleForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}))

    class Meta:
        model = Role
        fields = '__all__'

class DepartmentForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}))
    location = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Location'}))

    class Meta:
        model = Department
        fields = '__all__'