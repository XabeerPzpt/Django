from django.contrib import admin
from .models import Teacher, Course, Student

admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(Course)
# Register your models here.
