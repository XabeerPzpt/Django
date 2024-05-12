from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator


class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.user.username
class Student(models.Model):
    fullname = models.CharField(max_length=50, null=False)
    Address = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    phone_number = models.CharField(max_length=10)
    course = models.ForeignKey("Course", null=True, on_delete=models.SET_NULL ,default=0)
    def __str__(self):
        return self.fullname
class Course(models.Model):
    cid=models.AutoField(primary_key=True)
    course_name = models.CharField(null=False, max_length=50)
    price = models.IntegerField()
    Months_duration = models.IntegerField()
    def __str__(self):
        return self.course_name