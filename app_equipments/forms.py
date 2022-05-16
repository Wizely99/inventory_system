from django.forms import ModelForm
from django import forms
from app_equipments.models import add_equipment

class add_equipment_form(ModelForm):
    class Meta:
        model=add_equipment
        fields='__all__'
        verbose_name = 'equipment'
        verbose_name_plural = 'equipments'
        # db_table = 'music_album'
        # exclude = ('status',)
        widgets = {
               'status': forms.RadioSelect()
           }  