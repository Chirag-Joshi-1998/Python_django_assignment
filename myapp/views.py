from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from .models import Doctor,Profile
from .forms import DoctorForm,RegisterForm, ProfileForm
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def home(request):
    return render(request,'myapp/home.html')

def register(request):
    return render(request, 'myapp/register.html')

# READ: Display all doctors
def doctor_list(request):
    doctors = Doctor.objects.all()  # Fetch all doctors from the database
    return render(request, 'myapp/doctor_list.html', {'doctors': doctors})


def doctor_list_ajax(request):
    doctors = Doctor.objects.all()
    return render(request, 'myapp/doctor_list_ajax.html', {'doctors': doctors})

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


# CREATE: Add a new doctor using ajax
@csrf_exempt
def add_doctor_ajax(request):
    if request.method == "POST":
        data = json.loads(request.body)
       
        doctor = Doctor.objects.create(
            name=data['name'],
            specialty=data['specialization'],
            experience=data['experience'],
            contact=data['contact'],
            availability=data['availability'],
            clinic_address=data['clinic_address']
        )
       
        return JsonResponse({'message': 'Doctor added successfully!', 'doctor_id': doctor.id})


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

# UPDATE: Edit doctor details using Ajax
def edit_doctor_ajax(request, doctor_id):
    doctor = get_object_or_404(Doctor, id=doctor_id)
    if request.method == "POST":
        data = json.loads(request.body)
        doctor.name=data['name']
        doctor.specialization=data['specialization']
        doctor.experience=data['experience']
        doctor.contact=data['contact']
        doctor.availability=data['availability']
        doctor.clinic_address=data['clinic_address']
        doctor.save()
        return JsonResponse({'message': 'Doctor updated successfully!'})
    



# DELETE: Remove a doctor
def delete_doctor(request, pk):
    doctor = get_object_or_404(Doctor, pk=pk)
    if request.method == "POST":
        doctor.delete()
        return redirect('doctor_list')
    return render(request, 'myapp/delete_doctor.html', {'doctor': doctor})

# DELETE: Remove a doctor using Ajax
def delete_doctor_ajax(request, doctor_id):
    doctor = get_object_or_404(Doctor, id=doctor_id)
    doctor.delete()
    return JsonResponse({'message': 'Doctor deleted successfully!'})


def profile(request):
    return render(request,'myapp/profile.html')

def contactus(request):
    return render(request,'myapp/contactus.html')



# Register a new user
def user_register(request):
    if request.method == "POST":
        user_form = RegisterForm(request.POST)
        profile_form = ProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data['password'])
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            login(request, user)
            return redirect('dashboard')
    else:
        user_form = RegisterForm()
        profile_form = ProfileForm()
    return render(request, 'myapp/user_register.html', {'user_form': user_form, 'profile_form': profile_form})


# User login
def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'myapp/login.html', {'form': form})

# User logout
def user_logout(request):
    logout(request)
    return redirect('login')

# User dashboard
@login_required
def dashboard(request):
    return render(request, 'myapp/dashboard.html')

# Password change
@login_required
def change_password(request):
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Prevents logout after password change
            return redirect('dashboard')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'myapp/change_password.html', {'form': form})


