from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['id', 'points']

class UserSerializer(serializers.HyperlinkedModelSerializer):
    profile = ProfileSerializer()
    
    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'profile']