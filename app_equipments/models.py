from django.db import models
from django.utils import timezone
class hospital_department(models.Model):
    departments = models.CharField(max_length=255)
    classes=models.CharField(max_length=255)
    created_at= models.DateTimeField(editable=False,null=True)
    modified=models.DateTimeField(blank=True,null=True,)

    class Meta:
        verbose_name = 'department'
        verbose_name_plural = 'departments'
        db_table='departments'
        order_with_respect_to = 'created_at'
    def __str__(self):
        return self.departments
    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = timezone.now()
        self.modified = timezone.now()
        super(hospital_department, self).save(*args, **kwargs)

class add_equipment(models.Model):
    STATUS_CHOICES = (('1','working'),('0','faulty'))
    model=models.CharField(max_length=255,)
    brand  = models.CharField(max_length=255)
    ppmperiod= models.IntegerField()
    status= models.CharField(max_length=1,choices=STATUS_CHOICES,default='1' )
    serial_number= models.CharField(max_length=255,primary_key=True)
    created_at= models.DateTimeField(editable=False,null=True)
    modified=models.DateTimeField(blank=True,null=True,)
    department=models.ForeignKey(hospital_department,on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return self.model
    class Meta:
        verbose_name = 'equipment'
        verbose_name_plural = 'equipments'
        ordering=['created_at','modified']
        # ordering=['status','department']
        db_table='equipments'
    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = timezone.now()
        self.modified = timezone.now()
        super(add_equipment, self).save(*args, **kwargs)
            
            
              
                

