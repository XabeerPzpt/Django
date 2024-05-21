from django.contrib import admin
from .models import Teacher, Course, Student, Attendance, TotalAttendance

class StudentAdmin(admin.ModelAdmin):
    list_display= ('fullname', 'course1', 'course2', 'course3')
    list_filter = ('course1', 'course2', 'course3')

class AttendanceRecord(admin.ModelAdmin):
    list_filter = ('student','date')
admin.site.register(Teacher)
admin.site.register(Student,StudentAdmin)
admin.site.register(Course)
admin.site.register(Attendance,AttendanceRecord)
admin.site.register(TotalAttendance)
# Register your models here.
