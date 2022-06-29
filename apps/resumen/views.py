from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from ..players.models import Player
from ..players.serializers import PlayerSerializer
from ..teams.models import Team
from ..teams.serializers import TeamSerializer
from ..staff.models import CoachingStaff
from ..staff.serializers import CoachingStaffSerializer


class ResumenApiView(APIView):
    def get(self, request, *args, **kwargs):
        context = {
            'Total Equipos registrados' : Team.objects.all().count(),
            'Total Jugadores registrados': Player.objects.all().count(),
            'Jugador mas joven del toreno': PlayerSerializer(Player.objects.younger_player()).data,
            'Jugador con mas edad del toreno': PlayerSerializer(Player.objects.older_player()).data,
            'Total jugadores suplentes en el toreno' : Player.objects.count_substitutes(),
            'Promedio de jugadores suplentes en cada equipo': Team.objects.avg_sustitutes_players(),
            'Equipo con mas jugadores registrados': TeamSerializer(Team.objects.team_most_players()).data,
            'Edad promedio de los jugadores': Player.objects.avg_age(),
            'Promedio de numeros de jugadores por equipos': Team.objects.avg_players(),
            'Director tecnico con mas edad' : CoachingStaffSerializer(CoachingStaff.objects.older_coach()).data
        }
        return Response(context)


