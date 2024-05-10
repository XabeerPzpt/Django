from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator


class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.user.username
class Student(models.Model):
    Fullname = models.CharField(max_length=50)
    Address = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    phone_number = models.CharField(max_length=10)
    courses = models.ManyToManyField("Course", related_name="student")
    def __str__(self):
        return self.Fullname
class Course(models.Model):
    course_name = models.CharField(primary_key=True,null=False, max_length=50)
    price = models.IntegerField()
    Duration = models.IntegerField()
    students = models.ManyToManyField("Student", related_name="course")
    def __str__(self):
        return self.course_name