from django.db import models 
 
# Create your models here. 
class Clubs(models.Model): 
    name=models.CharField(max_length=50, verbose_name="Club name") 
    description=models.TextField(verbose_name="Description", blank=True, null=True) 
    contact_email=models.EmailField(verbose_name="Contact email", blank=True,null=True) 
    image=models.ImageField(verbose_name="Club Image", upload_to='Clubs/', blank=True, null=True) 
 
    def __str__(self) -> str: 
        return self.name 