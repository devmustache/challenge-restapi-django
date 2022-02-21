from dataclasses import fields
from rest_framework import serializers
from core.models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['id', 'firstName', 'lastName', 'age', 'sex']
