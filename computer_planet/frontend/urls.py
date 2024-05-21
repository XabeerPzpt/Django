from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.homepage , name='home'),
    path('aboutUs/', views.about , name='aboutUs'),
    path('courses/', views.courses , name='courses'),
    path('gallery/', views.gallery , name='gallery'),
    path('services/', views.services , name='services'),
    path('login/', views.login_view, name='login'),
    path('attendance/', views.attendance , name='attendance'),
    path('attendance/<int:student_id>', views.getstudent , name='getstudent'),
    path('attendance_report', views.attendance_report , name='attendance_report'),
    path('individual_report/<int:student_id>', views.individual_report , name='individual_report'),
]
 