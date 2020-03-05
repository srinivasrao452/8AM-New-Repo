
from django.contrib import admin

from .models import Student,Employee

class StudentAdmin(admin.ModelAdmin):
    list_display = ['num','name','location','marks']

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['num','name','location','salary']

admin.site.register(Student,StudentAdmin)
admin.site.register(Employee,EmployeeAdmin)