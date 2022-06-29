from django.db import models
from django.db.models.functions import ExtractDay, ExtractMonth, ExtractYear
from datetime import date, timedelta, datetime

class PlayerManager(models.Manager):
    
    def younger_player(self):
        return self.all().order_by('-date_born')[0]
    
    def older_player(self):
        return self.all().order_by('date_born')[0]
    
    def count_suplents(self):
        return self.filter(titular=False).count()
    
    def avg_age(self):
        return (
                self.annotate(age=datetime.now().year - ExtractYear('date_born'))
                .aggregate(models.Avg('age'))
            )
    
    
    
