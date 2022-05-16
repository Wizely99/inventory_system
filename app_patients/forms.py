       
from django import forms

from app_patients.models import patient
from app_users.forms import DatePickerInput


class patient_form(forms.ModelForm):
    class Meta:
        model=patient
        fields=('card_number','username','registered_by','first_name', 'last_name','gender','birth_date','marital_status', 'phone_number','email',)
        widgets={
            'gender':forms.RadioSelect(),
            'marital_status':forms.RadioSelect(),
            'birth_date':DatePickerInput(),
        }