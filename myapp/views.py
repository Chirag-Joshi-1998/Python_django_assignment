from django.shortcuts import render, get_object_or_404, redirect
from .models import Doctor
from .forms import DoctorForm


# Create your views here.

def home(request):
    return render(request,'myapp/home.html')

def register(request):
    return render(request, 'myapp/register.html')

# READ: Display all doctors
def doctor_list(request):
    doctors = Doctor.objects.all()  # Fetch all doctors from the database
    return render(request, 'myapp/doctor_list.html', {'doctors': doctors})


# CREATE: Add a new doctor
def add_doctor(request):
    if request.method == "POST":
        form = DoctorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('doctor_list')
    else:
        form = DoctorForm()
    return render(request, 'myapp/add_doctor.html', {'form': form})


# UPDATE: Edit doctor details
def edit_doctor(request, pk):
    doctor = get_object_or_404(Doctor, pk=pk)
    if request.method == "POST":
        form = DoctorForm(request.POST, instance=doctor)
        if form.is_valid():
            form.save()
            return redirect('doctor_list')
    else:
        form = DoctorForm(instance=doctor)
    return render(request, 'myapp/edit_doctor.html', {'form': form})


# DELETE: Remove a doctor
def delete_doctor(request, pk):
    doctor = get_object_or_404(Doctor, pk=pk)
    if request.method == "POST":
        doctor.delete()
        return redirect('doctor_list')
    return render(request, 'myapp/delete_doctor.html', {'doctor': doctor})


def profile(request):
    return render(request,'myapp/profile.html')

def contactus(request):
    return render(request,'myapp/contactus.html')