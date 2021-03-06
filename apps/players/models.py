from django.db import models
from ..teams.models import Team
from .managers import PlayerManager
# Utils
from .sources.choices import PLAYER_POSITIONS
from datetime import date

class Player(models.Model):
    id = models.AutoField(primary_key=True)
    player_img = models.ImageField(upload_to='img/players')
    name = models.CharField(max_length=50,  verbose_name='Nombre del jugador')
    last_name = models.CharField(max_length=50, verbose_name='Apellido del jugador')
    date_born = models.DateField(verbose_name="Fecha de nacimiento del jugador")
    position = models.CharField(max_length=4, choices=PLAYER_POSITIONS, verbose_name='Posicion en el campo de juego')
    number_jersey = models.IntegerField(verbose_name='Numero del dorsal del jugador')
    titular = models.BooleanField(default=False)
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    team = models.ForeignKey(Team, null=False, on_delete=models.CASCADE, related_name='players', verbose_name='Seleccion')
    # Manager 
    objects = PlayerManager()

    class Meta:
        db_table = 'player'
        verbose_name = "Player"
        verbose_name_plural = "Players"


    def __str__(self):
        return self.name
    
    

