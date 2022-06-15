from rest_framework import serializers
from .models import Profile,Project
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model=Profile
        fields=('profile','bio','user','contact')

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model=Project
        fields=('name','link','description','date')