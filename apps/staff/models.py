from django.db import models
from ..teams import models
# Create your models here.
class RolStaff(models.Model):
    id_staff = models.AutoField(primary_key=True)
    rol_description = models.CharField(max_length=250,unique=True)
    
    class Meta:
        db_table = 'rolstaff'
        verbose_name = "RolStaff"
        verbose_name_plural = "RolStaffs"

    def __str__(self):
        return self.name



class CoachingStaff(models.Model):
    id_staff = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250,unique=True)
    last_name = models.CharField(max_length=250,unique=True)
    date_born = models.DateField()
    rol = models.ForeignKey(RolStaff, on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)    
    
    team = models.ForeignKey(models.Team, on_delete=models.CASCADE)

    class Meta:
        db_table = 'coachingstaff'
        unique_together = ['name', 'last_name']
        verbose_name = "CoachingStaff"
        verbose_name_plural = "CoachingStaffs"
        

    def __str__(self):
        return self.name

