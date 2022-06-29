from rest_framework import serializers
from .models import Team

class TeamSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Team
        fields = ('id_team', 'name', 'img_flag', 'img_shield')
        # fields = '__all__'
        
    