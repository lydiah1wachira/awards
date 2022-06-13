from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    profile_pic=models.ImageField(upload_to = 'profile/')
    name = models.CharField(blank=True, max_length=120)
    bio=models.CharField(max_length=60)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    contact=models.EmailField(max_length=100, blank=True)
   
    
