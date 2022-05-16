from django.forms import model_to_dict
from django.http import HttpResponse
from django.shortcuts import render

from app_patients.models import patient


# Create your views here.
def view_profile(request,username):
    if username:
        data=patient.objects.filter(username=username)
        new_data=data.values('first_name', 'last_name','marital_status', 'phone_number','email','username')[0]
        return render(request, 'app_patients/profile.html',{'new_data':new_data})
    else:
        print(request.user,username)
        return HttpResponse('your are not authorised')
