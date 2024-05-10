from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.homepage , name='base'),
    path('aboutUs/', views.about , name='aboutUs'),
    path('courses/', views.courses , name='courses'),
    path('gallery/', views.gallery , name='gallery'),
    path('services/', views.services , name='services'),
    path('login/', views.login_view, name='login'),
    path('attendance/', views.attendance , name='attendance'),
]
