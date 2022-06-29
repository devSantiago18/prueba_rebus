from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import CoachingStaff
from .serializers import CoachingStaffSerializer

class StaffDetailView(APIView):
    def get(self, request, id_staff):
        staff = CoachingStaff.objects.get(id_staff=id_staff)
        serializer = CoachingStaff(staff)
        return Response(serializer.data)


class StaffApiView(APIView):
    def get(self, request):
        staff = CoachingStaff.objects.all()
        serializer = CoachingStaffSerializer(staff, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = CoachingStaffSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"succes":"The team has been created succesfully"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, id_staff, format=None):
        staff = CoachingStaff.objects.get(id_staff=id_staff)
        serializer = CoachingStaffSerializer(staff, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"succes":"The team has been updated succesfully"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id_staff, format=None):
        staff = CoachingStaff.objects.get(id_staff=id_staff)
        staff.delete()
        return Response({"succes":"The team has been deleted succesfully"}, status=status.HTTP_200_OK)
    
