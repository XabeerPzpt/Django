from django.contrib import admin
from .models import Teacher, Course, Student

class StudentAdmin(admin.ModelAdmin):
    list_display= ('fullname', 'course1', 'course2', 'course3')
    list_filter = ('course1', 'course2', 'course3')
admin.site.register(Teacher)
admin.site.register(Student,StudentAdmin)
admin.site.register(Course)
# Register your models here.
