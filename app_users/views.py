from datetime import date, datetime
from django.shortcuts import render,redirect
from django.http import HttpResponse
from app_patients.forms import patient_form
from app_patients.models import patient
from app_users.forms import login_form
from django.contrib.auth import authenticate,login
from django.http import HttpResponse
from .models import User
from django.contrib.auth import logout
from .forms import signupForm
import math
from django.views.generic.edit import FormView

from django.contrib import messages


# Create your views here.
 # age=date.today() - birthdate

def signup(request):
    if request.method == 'POST':
        print(request.FILES)
        new_user=signupForm(request.POST,request.FILES)
        if new_user.is_valid():
            new_user.save()
            messages.success(request, "Account created successfully")
            
            return redirect('login')
            
        else:
            print(new_user.errors)
            context={'form':new_user}
            messages.error(request, "wrong credentials")
            
            return render(request, 'app_users/signup_form.html',context)
            
    form=signupForm()
    context={'form':form}
    return render(request, 'app_users/signup_form.html',context)
def login_user(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=username,password=password)
        
        if user is not None:
            login(request,user)
            messages.success(request, "login successfully")
            
            return redirect('dashboard')
        else:
            user=patient.objects.filter(username=username,)
            # login(request,user)
            print(user.values())
            if user.password==password:
                return redirect('view_profile',username=username)
        
            
    else:
        return render(request, 'app_users/login.html')
    
def logout_user(request):
    logout(request)
    return redirect('login')


class AddPatient(FormView):
    form_class = patient_form
    template_name = 'app_patients/registration_form.html'
    success_url = '/users/add_patient'
    def form_valid(self, form):
        form.save()
        # form.send_email()
        return super().form_valid(form)
    def form_invalid(self, form):
        return super().form_valid(form)
        
    