from rest_framework import serializers
from .models import Player

class PlayerSerializer(serializers.Serializer):
    
    class Meta:
        model = Player
        fields = '__all__'