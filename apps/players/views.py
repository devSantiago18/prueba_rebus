from rest_framework import viewsets
# models
from .models import Player
from .serializers import PlayerSerializer
class PlayerViewSet(viewsets.ModelViewSet):
    serializer_class = PlayerSerializer
    queryset = Player.objects.all()
