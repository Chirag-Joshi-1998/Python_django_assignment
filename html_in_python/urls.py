"""
URL configuration for html_in_python project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('register/', views.register, name='register'),
    path('doctorlist/', views.doctor_list, name='doctor_list'),
    path('profile/', views.profile, name='profile'),
    path('contactus/', views.contactus, name='contactus'),
    path('add/', views.add_doctor, name='add_doctor'),
    path('edit/<int:pk>/',views.edit_doctor, name='edit_doctor'),
    path('delete/<int:pk>/', views.delete_doctor, name='delete_doctor'),
    path('user_register/', views.user_register, name='user_register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('change-password/', views.change_password, name='change_password'),
    #ajax
    path('doctorlist_ajax/', views.doctor_list_ajax, name='doctor_list_ajax'),

    path('add_ajax/', views.add_doctor_ajax, name='add_doctor_ajax'),
    path('edit_ajax/<int:doctor_id>/', views.edit_doctor_ajax, name='edit_doctor_ajax'),
    path('delete_ajax/<int:doctor_id>/', views.delete_doctor_ajax, name='delete_doctor_ajax'),




]


    
