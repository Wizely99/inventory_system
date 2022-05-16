from django import forms
from django.forms import ModelForm
from app_users.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

class  DatePickerInput(forms.DateInput):
    input_type='date'
# User=get_user_model()

class login_form(ModelForm):
    class Meta:
        model=User
        fields=['username', 'password',]


class signupForm(UserCreationForm):
    class Meta:
        model=User
        fields=('first_name', 'last_name','gender','birth_date','marital_status', 'phone_number','email','username','password1','profile_pic','password2',)
        widgets={
            'gender':forms.RadioSelect(),
            'marital_status':forms.RadioSelect(),
            'birth_date':DatePickerInput(),
        }
 
    