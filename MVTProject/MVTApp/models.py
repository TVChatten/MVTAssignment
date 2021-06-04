from django.db import models
from datetime import datetime

from django.db.models.fields import CharField
# Create your models here.
class School(models.Model):
    name = models.CharField(max_length=400)

    def __str__(self):
        return self.name

class Certificate_Type(models.Model):
    certificate_type = models.CharField(max_length=400)

    def __str__(self):
        return self.certificate_type

class Grade(models.Model):
    grade = models.CharField(max_length=1)

    def __str__(self):
        return self.grade

class Faculty(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Department(models.Model):
    dept_name = models.CharField(max_length=50)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)

    def __str__(self):
        return self.dept_name

class Student(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE)
    certificate_type = models.ForeignKey(Certificate_Type, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=50)
    year_of_graduation = models.IntegerField()

    def __str__(self):
        return self.full_name


