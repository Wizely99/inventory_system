from datetime import date
from django.db import models
from app_users.helpers import calc_age

from app_users.models import User


# Create your models here.
class patient(User):
    registered_by=models.ForeignKey(User, on_delete=models.RESTRICT,related_name='registered')
    is_patient=models.BooleanField(default=True)
    card_number = models.CharField(primary_key=True, max_length=255)
    class Meta:
        db_table='patients'
        app_label='app_users'
        verbose_name = 'patient'
        verbose_name_plural= 'patients'
    def save(self, *args, **kwargs):
        if self.birth_date  is None:
           self.age='none'
           self.birth_date = date.today()    
        self.age=calc_age(self.birth_date)
        self.is_staff=False
        self.is_biomed_eng=False
        self.is_admin=False
        print(self.username)
        if self.username is None:
            self.username=self.card_number
        super(User, self).save(*args, **kwargs)