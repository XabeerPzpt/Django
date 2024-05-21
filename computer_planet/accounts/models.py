from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
import datetime

date = datetime.datetime.now().date
class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.user.username
class Student(models.Model):
    fullname = models.CharField(max_length=50, null=False)
    Address = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    phone_number = models.CharField(max_length=10)
    course1 = models.ForeignKey("Course",null=True, on_delete=models.SET_NULL, blank=True, related_name="course1")
    course2 = models.ForeignKey("Course",null=True, on_delete=models.SET_NULL, blank=True, related_name="course2")
    course3 = models.ForeignKey("Course",null=True, on_delete=models.SET_NULL, blank=True, related_name="course3")
  
    def __str__(self):
        return self.fullname
class Course(models.Model):
    cid=models.AutoField(primary_key=True)
    course_name = models.CharField(null=False, max_length=50)
    price = models.IntegerField()
    Months_duration = models.IntegerField()
    def __str__(self): 
        return self.course_name
class TotalAttendance(models.Model):
    student = models.OneToOneField(Student,on_delete=models.CASCADE)
    total_days_present = models.PositiveIntegerField(null=False,default=0)
    def __str__(self):
        return f"Total present days of {self.student.fullname} = {self.total_days_present}"

class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True, null=True )
    is_present = models.CharField(max_length=7)
    def __str__(self):
        return f"{self.student.fullname} - {self.date} = {self.is_present}"
