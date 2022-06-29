from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework import status
from .models import Team
from .serializers import TeamSerializer

# generics views
class TeamsListView(ListAPIView):
    
    serializer_class = TeamSerializer
    
    
    def get_queryset(self):
        return Team.objects.all()

class TeamsCreateView(CreateAPIView):
    serializer_class = TeamSerializer
    
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"succes":"The team has been created succesfully"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    
    
    
    def get_queryset(self):
        return Team.objects.all()

class TeamDetailView(APIView):
    
    
    def get(self, request, id_team):
        team = Team.objects.get(id_team=id_team)
        serializer = TeamSerializer(team)
        return Response(serializer.data)


# ApiView
class TeamApiView(APIView):
    
    
    def get(self, request):
        team = Team.objects.all()
        serializer = TeamSerializer(team, many=True)
        return Response(serializer.data)

    
    def post(self, request, format=None):
        serializer = TeamSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"succes":"The team has been created succesfully"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
    def put(self, request, id_team, format=None):
        team = Team.objects.get(id_team=id_team)
        serializer = TeamSerializer(team, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"succes":"The team has been updated succesfully"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, id_team, format=None):
        team = Team.objects.get(id_team=id_team)
        team.delete()
        return Response({"succes":"The team has been deleted succesfully"}, status=status.HTTP_200_OK)
    

    
