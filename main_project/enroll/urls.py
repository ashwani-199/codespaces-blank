from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_emp, name='enroll.all_emp'),
    path('add_role', views.add_role, name='enroll.add_role'),
    path('add_dept', views.add_dept, name='enroll.add_dept'),
    path('add_emp', views.add_emp, name='enroll.add_emp'),
    path('remove_emp/<int:id>', views.remove_emp, name='enroll.remove_emp'),
]