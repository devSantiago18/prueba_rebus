from rest_framework import serializers
from .models import CoachingStaff

class CoachingStaffSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CoachingStaff
        fields = '__all__'