from django.db import models
from .managers import StaffCoachManager
from ..teams.models import Team
from .sources.choices import  COUNTRY_CHOICES, ROL_STAFF


class CoachingStaff(models.Model):
    id_staff = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250,unique=True)
    last_name = models.CharField(max_length=250,unique=True)
    date_born = models.DateField()
    nationality = models.CharField(max_length=5, choices=COUNTRY_CHOICES, null=True)
    rol = models.CharField(max_length=250, choices=ROL_STAFF)
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)        
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    # My managers
    coachs = StaffCoachManager()

    class Meta:
        db_table = 'coachingstaff'
        unique_together = ['name', 'last_name']
        verbose_name = "CoachingStaff"
        verbose_name_plural = "CoachingStaffs"
        

    def __str__(self):
        return self.name

