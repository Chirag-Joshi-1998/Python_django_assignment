from django.shortcuts import render
from .models import Doctor

# Create your views here.

def home(request):
    return render(request,'myapp/home.html')

def register(request):
    return render(request, 'myapp/register.html')


def doctor_list(request):
    doctors = Doctor.objects.all()  # Fetch all doctors from the database
    return render(request, 'myapp/doctor_list.html', {'doctors': doctors})

def profile(request):
    return render(request,'myapp/profile.html')

def contactus(request):
    return render(request,'myapp/contactus.html')