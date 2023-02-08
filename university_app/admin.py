from django.contrib import admin
from .models import *


# Register your models here.


@admin.register(Test)
class TestAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Test._meta.fields]


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Student._meta.fields]


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Course._meta.fields]


#  Staff, Role
@admin.register(College)
class CollegeAdmin(admin.ModelAdmin):
    list_display = [f.name for f in College._meta.fields]


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Department._meta.fields]


@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Staff._meta.fields]


@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Role._meta.fields]
