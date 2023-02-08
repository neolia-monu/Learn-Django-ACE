from rest_framework import serializers
from .models import *


class CourseSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50)
    duration = serializers.DecimalField(max_digits=5, decimal_places=2)


#  COURSE , COLLEGE, DEPARTMENT, STAFF, ROLE, STUDENT
class CollegeSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=200)
    code = serializers.IntegerField()
    course_name = serializers.CharField(source='course.name', read_only=True)
    # course = CourseSerializer()


class DepartmentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50)
    course_name = serializers.CharField(source='course.name', read_only=True)
    # course = CourseSerializer()


class RoleSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=30)


class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    course_name = serializers.CharField(source='course.name', read_only=True)
    college_name = serializers.CharField(source='college.name', read_only=True)
    department_name = serializers.CharField(source='department.name', read_only=True)
    
    # college = serializers.SerializerMethodField()
    # deartment = serializers.SerializerMethodField()
    # course = serializers.SerializerMethodField()
    
    # college = CollegeSerializer()
    # department = DepartmentSerializer()
    # course = CourseSerializer()

    def create(self, validated_data):
        print(validated_data)
        return Student.objects.create(**validated_data)


class StaffSerializer(serializers.Serializer):
    name = models.CharField(max_length=100)
    department = serializers.CharField(source='department.name')
    role = serializers.CharField(source='role.name')
    college = serializers.CharField(source='college.name')
    course = serializers.CharField(source='course.name')
    # department = DepartmentSerializer()
    # role = RoleSerializer()
    # college = CollegeSerializer()
    # course = CourseSerializer()

