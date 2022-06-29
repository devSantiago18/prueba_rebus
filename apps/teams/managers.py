from django.db import models

class TeamsManager(models.Manager):
        
    def team_most_players(self):
        return self.all().annotate(player_count=models.Count('players')).order_by('-player_count').first()

    
