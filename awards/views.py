from django.shortcuts import render,redirect,get_object_or_404
from .models import Profile,Project
from django.http import HttpResponse,Http404,HttpResponseRedirect,JsonResponse
from .forms import SignUpForm,PostForm
from django.contrib.auth import login, authenticate,logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
  '''View function to display the index page and its data'''
  
  try:
    projects = Project.objects.all()
  except Exception as e :
    raise  Http404()
      
  return render(request, 'index.html', {"projects":projects})

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form':form})
  

def logout_view(request):
    logout(request)
    return redirect('index')
  
@login_required(login_url='login')
def post(request):
    current_user=request.user
    if request.method=='POST':
        form =PostForm(request.POST,request.FILES)
        if form.is_valid():
            post=form.save(commit=False)
            post.user=current_user
            post.save()
        return redirect("index")
    else:
        form=PostForm()
    return render(request,'post.html',{'form':form})