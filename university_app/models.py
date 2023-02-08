from django.db import models


# Create your models here.


class Test(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.id} {self.name} {self.created_at}"


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class Course(BaseModel):
    name = models.CharField(max_length=50, unique=True)
    duration = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.name} and {self.duration}"


class College(BaseModel):
    name = models.CharField(max_length=200, unique=True)
    code = models.IntegerField(unique=True)

    def __str__(self):
        return f"{self.name}, {self.code}"

class College_Course(models.Model):
    college = models.ForeignKey(to=College, on_delete=models.PROTECT) 
    course = models.ForeignKey(to=Course, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.college.name}, {self.course.name}"

class Department(BaseModel):
    name = models.CharField(max_length=50, unique=True)
    course = models.ForeignKey(to=Course, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.name}, {self.course.name}"


class Role(BaseModel):
    name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return f"{self.name}"


class Student(BaseModel):
    name = models.CharField(max_length=100)
    college = models.ForeignKey(to=College, related_name='student', on_delete=models.PROTECT)
    department = models.ForeignKey(to=Department, related_name='student', on_delete=models.PROTECT)
    course = models.ForeignKey(to=Course, related_name='student', on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.name}, {self.college.name}, {self.department.name}, {self.course.name}"


class Staff(BaseModel):
    name = models.CharField(max_length=100)
    department = models.ForeignKey(to=Department, on_delete=models.PROTECT)
    role = models.ForeignKey(to=Role, on_delete=models.PROTECT)
    college = models.ForeignKey(to=College, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.name}, {self.department.name}, {self.role.name}, {self.college.name}"

class Staff_Course(models.Model):
    staff = models.ForeignKey(to=Staff, on_delete=models.PROTECT)
    course = models.ForeignKey(to=Course, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.staff.name}, {self.course.name}"