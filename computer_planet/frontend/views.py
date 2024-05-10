from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
def homepage(request):
    return render(request,'base.html')
def about(request):
    return render(request,'aboutUs.html')
def courses(request):
    return render(request,'courses.html')
def gallery(request):
    return render(request,'gallery.html')
def services(request):
    return render(request,'services.html')
def dashboard(request):
    return render(request,'dashboard.html')
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to dashboard or any other page after successful login
            return redirect('dashboard')
        else:
            # Return an error message or render the login form again with an error message
            return render(request, 'login.html', {'error_message': 'Invalid username or password.'})
    else:
        return render(request, 'login.html')