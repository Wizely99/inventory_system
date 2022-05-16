from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.db.models import Count
from django.contrib import messages
from django.contrib.auth.decorators import login_required      


from app_equipments.models import hospital_department,add_equipment
from .forms import add_equipment_form

def add_equipment_handler(request):
    if request.method == 'GET':
        context={'form':add_equipment_form}
        return render(request, 'app_equipments/add_equipment.html', context)
    else:
        new_equipment =add_equipment_form(request.POST)
        if new_equipment.is_valid():
            new_equipment.save()
            messages.success(request,'equipment added')
            return redirect('dashboard')
        else:
            context={'form':new_equipment}
            return render(request, 'app_equipments/add_equipment.html', context)
@login_required(login_url='/users/login')
def dashboard_handler(request):
    if request.method == 'GET':
        departments=hospital_department.objects.all()
        departmento=hospital_department.objects.annotate(Count('add_equipment'))
        array_count=[]
        for department in departments:
            count = add_equipment.objects.filter(department=department)
            array_count.append({department.departments: [len(count),department.classes]})
        context={'departments':array_count}
        return render(request, 'dashboard.html',context) 
@login_required(login_url='/users/login')
def departmental_request_handler(request,pk):
    if request.method =='POST':
        departmental_equipments=add_equipment.objects.filter(department=pk)
        return render(request, 'app_equipments/departmental_equipments.html',departmental_equipments)
            