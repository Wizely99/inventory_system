from datetime import date, datetime
import math
from tabnanny import verbose
from django.db import models
from django import forms
from django.core.validators import RegexValidator

from app_equipments.models import hospital_department
from django.contrib.auth.models import AbstractUser

from app_users.helpers import calc_age

# Create your models here.


# def user_directory_path(instance, filename):
  
#     # file will be uploaded to MEDIA_ROOT / user_<id>/<filename>
#     return f'user_{0}/{1}'
class User(AbstractUser):
    # department=models.ForeignKey('hospital_department',on_delete=models.CASCADE)
    is_admin=models.BooleanField(default=False)
    is_biomed_eng=models.BooleanField(default=False)
    is_staff=models.BooleanField(default=True)
    age=models.CharField(max_length=25)
    email=models.EmailField()
    first_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    Phone_number_validator=RegexValidator(regex=r'[0]{1}[6-7]{1}[0-9]{8}',message='enter a valid phone number ')
    phone_number=models.CharField(validators=[Phone_number_validator],max_length=10)
    profile_pic=models.ImageField(upload_to='profile_pics/', height_field=None, width_field=None, max_length=255,blank=True)
    
    GENDER = (
        ('1', 'male'),
        ('0', 'female'),
    )
    gender = models.CharField(max_length=1, choices=GENDER,default='1')
    MARITAL_STATUS = (
        ('S', 'single'),
        ('M', 'married'),
        ('D', 'divorced'),
        ('D', 'divorced'),
    )
    marital_status = models.CharField(max_length=1,choices=MARITAL_STATUS,default='S')
    birth_date = models.DateField()
    agreement=models.BooleanField(default=False)
    class Meta:
        swappable = 'AUTH_USER_MODEL'
        app_label = 'app_users'
        db_table='staff'
        verbose_name = 'staff'
        verbose_name_plural= 'staffs'                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   
    def __str__(self):
        return self.username
    def save(self, *args, **kwargs):
        if self.birth_date  is None:
           self.age='none'
           self.birth_date = date.today()
        else:
            self.age=calc_age(self.birth_date)
        super(User, self).save(*args, **kwargs)
    
