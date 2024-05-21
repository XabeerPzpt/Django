from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from accounts.models import *
from django.db.models import F
from django.utils import timezone

def homepage(request):
    return render(request,'home.html')

def about(request):
    return render(request,'aboutUs.html')

def courses(request):
    courses=Course.objects.all()
    return render(request,'courses.html',{'courses':courses})

def gallery(request):
    return render(request,'gallery.html')

def services(request):
    return render(request,'services.html')

def attendance(request):
    students = Student.objects.all()
    if request.method=='POST':
        date = timezone.now().date()
        for student in students:
            is_present = 'Present' if request.POST.get(f'present_{student.id}','off')=='present' else 'Absent'
            Attendance.objects.create(student=student,date=date, is_present=is_present)
            if is_present=='Present':
                summary, created = TotalAttendance.objects.get_or_create(student=student)
                summary.total_days_present = F('total_days_present')+1
                summary.save()
            else:
                summary, created = TotalAttendance.objects.get_or_create(student=student)
                summary.total_days_present = F('total_days_present')+0
                summary.save()
        return redirect('attendance_report')
    return render(request,'attendance.html',{'students':students})

def attendance_report(request):
    reports = TotalAttendance.objects.all().order_by('student_id')
    return render(request, 'attendance_report.html',{'reports':reports})

def individual_report(request, student_id):
    student = get_object_or_404(Student,id=student_id)
    records = Attendance.objects.filter(student=student).order_by('date')
    return(request, 'individual_report.html', {'records':records},{'student':student})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to dashboard or any other page after successful login
            return redirect('attendance')
        else:
            # Return an error message or render the login form again with an error message
            return render(request, 'login.html', {'error_message': 'Invalid username or password.'})
    else:
        return render(request, 'login.html') 
    
def getstudent(request, student_id):
    student = get_object_or_404(Student,id=student_id)
    return render(request, 'student_profile.html', {'student': student})

