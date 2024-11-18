from rest_framework import serializers
from .models import Event, Clubs

class EventSerializer(serializers.ModelSerializer):
    club = serializers.PrimaryKeyRelatedField(queryset=Clubs.objects.all()) 

    class Meta:
        model = Event
        fields = ['id', 'name', 'description', 'date', 'time', 'location', 'image', 'club']  
