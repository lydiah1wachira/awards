from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Profile(models.Model):
    profile_pic=models.ImageField(upload_to = 'profile/')
    name = models.CharField(blank=True, max_length=120)
    bio=models.CharField(max_length=60)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    contact=models.EmailField(max_length=100, blank=True)
    
    def __str__(self):
        return f'{self.user.username} Profile'
    
    class Meta:
        ordering = ['-profile_pic']

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)
    
    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()
        
        
class Project(models.Model):
    title=models.CharField(max_length=30)
    image=models.ImageField(upload_to='project/')
    content=models.IntegerField(default=0)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    description=models.TextField(max_length=320)
    link=models.URLField(max_length=60)
    date=models.DateField(auto_now=True)
    content=models.IntegerField(default=0)
    design=models.IntegerField(default=0)
    usability=models.IntegerField(default=0)
    
    
   

    class Meta:
        ordering=['-title']

    def __str__(self):
        self.title
        
    @classmethod
    def search_project(cls,title):
        searched=cls.objects.filter(title__icontains=title)
        return searched

   
class Comments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    text = models.CharField(max_length=200)
    pro_id = models.ForeignKey(Project, on_delete=models.CASCADE)
    def __str__(self):
        return self.text
    
    def save_comments(self):
        self.save()
    
    def delete_comments(self):
        self.delete()
    @classmethod 
    def all_comments(cls, id):
        comments = cls.objects.filter(project_id = id)
        return comments
    
class Rating(models.Model):
    design=models.PositiveIntegerField(default=0,validators=[MaxValueValidator(10)])
    usability=models.PositiveIntegerField(default=0,validators=[MaxValueValidator(10)])
    content=models.PositiveIntegerField(default=0,validators=[MaxValueValidator(10)])
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    project=models.IntegerField(default=0)