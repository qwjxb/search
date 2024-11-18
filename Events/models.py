from django.db import models
from Clubs.models import Clubs
# Create your models here.
class Event(models.Model): 
    name = models.CharField(max_length=255, verbose_name="Event name") 
    description = models.TextField(verbose_name="Description", blank=True, null=True) 
    date = models.DateField(verbose_name="Date") 
    time = models.TimeField(verbose_name="time", blank=True, null=True) 
    location = models.CharField(max_length=255, verbose_name="Place", blank=True, null=True) 
    image = models.ImageField(upload_to='events/', verbose_name="Poster", blank=True, null=True) 
    club = models.ForeignKey(Clubs, on_delete=models.CASCADE, verbose_name="Club", related_name="events") 
 
    def __str__(self): 
        return f"{self.name} - {self.club.name}"