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


]
