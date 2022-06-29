from django.db import models
class TeamsManager(models.Manager):
        
    def team_most_players(self):
        return self.all().annotate(player_count=models.Count('players')).order_by('-player_count').first()
    
    
    def avg_players(self):
        return self.all().annotate(player=models.Count('players')).aggregate(models.Avg('player'))


    def avg_sustitutes_players(self):
        return (self
                .all().annotate(player=models.Count('players', filter=models.Q(players__titular=False)))
                .aggregate(models.Avg('player'))
            )
