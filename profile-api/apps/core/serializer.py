from rest_framework import serializers
from core.models import Profile

class ProfileSerializer(serializers.ModelSerializer):

    firstName = serializers.CharField(source='first_name')
    lastName = serializers.CharField(source='last_name')
    
    class Meta:
        model = Profile
        fields = ['id', 'firstName', 'lastName', 'age', 'sex']
    
