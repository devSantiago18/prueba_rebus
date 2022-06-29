from django.db import models

class StaffCoachManager(models.Manager):
    
    
    def only_coach(self):
        return super().get_queryset().filter(rol=1)


    def older_coach(self):
        return self.filter(rol=1).order_by('date_born')[0]
    
    