from rest_framework import serializers
from .models import Player

class PlayerSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Player
        fields = ('id','name', 'last_name', 'date_born', 'age', 'position', 'number_jersey', 'titular', 'player_img')
        # fields = '__all__' 