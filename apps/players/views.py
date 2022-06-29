from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
# models
from .models import Player
from .serializers import PlayerSerializer
# util
from datetime import date, timedelta, datetime

class PlayerDetailView(APIView):
    
    
    def get(self, request, id, *args, **kwargs):
        player = Player.objects.get(id=id)
        serializer = PlayerSerializer(player)
        return Response(serializer.data)

class PlayerApiView(APIView): 
    
    
    def get(self, request, *args, **kwargs):
        player = Player.objects.all()
        serializer = PlayerSerializer(player, many=True)
        return Response(serializer.data)


    def post(self, request, *args, **kwargs):
        serializer = PlayerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"succes":"The player has been created succesfully"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    def put(self, request,id, *args, **kwargs):
        player = Player.objects.get(id=id)
        serializer = PlayerSerializer(player, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"succes":"The player has been updated succesfully"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    def delete(self, request, id,  *args, **kwargs):
        player = Player.objects.get(id=id)
        player.delete()
        return Response({"succes":"The player has been deleted succesfully"}, status=status.HTTP_200_OK)


