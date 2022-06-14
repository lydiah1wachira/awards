from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile,Project,Comments,Rating


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=255, help_text='Required. Input a valid email address!', required=True)
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        
    def save(self, commit=True):
        user= super (SignUpForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
    
class PostForm(forms.ModelForm):
    class Meta:
        model=Project
        exclude=['user','content']
        
class UpdateProfileForm(forms.ModelForm):
     class Meta:
        model=Profile
        exclude=['user']
        
        
class RatingsForm(forms.ModelForm):
    class Meta:
        model=Rating
        exclude=['user','project']
        
class ReviewsForm(forms.ModelForm):
    class Meta:
        model=Comments
        exclude=['user','pro_id']
