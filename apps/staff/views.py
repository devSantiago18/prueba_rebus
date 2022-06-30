from rest_framework import viewsets
from .models import CoachingStaff
from .serializers import CoachingStaffSerializer

class StaffViewSet(viewsets.ModelViewSet):
    serializer_class = CoachingStaffSerializer
    queryset = CoachingStaff.objects.all()
