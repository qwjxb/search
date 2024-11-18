from rest_framework import serializers
from .models import Clubs

class ClubSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clubs
        fields = ['id', 'name', 'description', 'contact_email', 'image'] 

