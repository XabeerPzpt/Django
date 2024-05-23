from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from accounts.models import *
from django.db.models import F
from django.utils import timezone
from datetime import timedelta

def homepage(request):
    today = timezone.now().date()
    yesterday = today - timedelta(days=1)
    todays_date, created = Today.objects.get_or_create(date=yesterday)        # recording today's date
    todays_date.date=today
    todays_date.save()
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



# for displaying attendance.html page
def attendance(request):
    today = Today.objects.first() 
    students = Student.objects.all()
    if request.method=='POST':
        date = timezone.now().date()
        for student in students:
            is_present = 'Present' if request.POST.get(f'present_{student.id}','off')=='present' else 'Absent'
            Attendance.objects.create(student=student,date=date, is_present=is_present)         # making attendance
            if is_present=='Present':
                summary, created = TotalAttendance.objects.get_or_create(student=student)      # Updating present days
                summary.total_days_present = F('total_days_present')+1
                summary.save()
            else:
                summary, created = TotalAttendance.objects.get_or_create(student=student)
                summary.total_days_present = F('total_days_present')+0
                summary.save()
        return redirect('attendance_report')
    return render(request,'attendance.html',{'students':students, 'today':today})

#For User page display:
def UserPage(request):
    return render(request, 'UserPage.html')

#For displaying Students fees:
def Fees(request):
    students=Student.objects.all()
    for student in students:        #Calculating Fees
        total_fee=0
        if student.course1:
            total_fee +=student.course1.price
        if student.course2:
            total_fee +=student.course2.price
        if student.course3:
            total_fee +=student.course3.price
        student.total_fee=total_fee
        student.save()
    return render(request, 'FeesPage.html',{'students':students})
#For displaying attendance report page after save button is clicked:
def attendance_report(request):
    reports = TotalAttendance.objects.all().order_by('student_id')
    return render(request, 'attendance_report.html',{'reports':reports})

#Display report of selected individuals
def individual_report(request, student_id):
    student = get_object_or_404(Student,id=student_id)
    records = Attendance.objects.filter(student=student).order_by('date')
    return render(request, 'individual_report.html', {'records':records,'student':student})

#For logging in user
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to dashboard or any other page after successful login
            return redirect('UserPage')
        else:
            # Return an error message or render the login form again with an error message
            return render(request, 'login.html', {'error_message': 'Invalid username or password.'})
    else:
        return render(request, 'login.html') 

# For Displaying selected student's profile    
def getstudent(request, student_id):
    student = get_object_or_404(Student,id=student_id)
    return render(request, 'student_profile.html', {'student': student})

