from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from accounts.models import Course, Student
from django.http import JsonResponse
from django.db.models import Q

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
    courses=Course.objects.all()
    return render(request,'attendance.html',{'courses':courses})
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
def getstudents(request):
    cid = request.GET.get('course_id')
    students = Student.objects.filter(Q(course1_id=cid) | Q(course2_id=cid) | Q(course3_id=cid))
    data = [{'fullname':students.fullname, 'address':students.address} for student in students]
    return JsonResponse(data, safe=False)
