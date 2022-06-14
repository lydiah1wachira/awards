from django.shortcuts import render,redirect,get_object_or_404
from .models import Profile,Project,Comments,Rating
from django.http import HttpResponse,Http404,HttpResponseRedirect,JsonResponse
from .forms import SignUpForm,PostForm,UpdateProfileForm, RatingsForm,ReviewsForm
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
            post.user=request.user
            post.save()
        return redirect("index")
    else:
        form=PostForm()
    return render(request,'post.html',{'form':form})
  
@login_required(login_url='login')
def profile(request):
    current_user=request.user
    try:
        prof=Profile.objects.filter(user=current_user)[0:1]
        user_projects=Project.objects.filter(user=current_user)
    except Exception as e:
        raise  Http404()
    if request.method=='POST':
        form=UpdateProfileForm(request.POST,request.FILES)
        if form.is_valid():
            profile=form.save(commit=False)
            profile.user=request.user
            profile.save()
        return redirect('profile')
    else:
        form=UpdateProfileForm()
    return render(request,'profile.html', {'form':form,'profile':prof,'projects':user_projects})

def project_detail(request,project_id):
    try:
        projects=Project.objects.filter(id=project_id)
        all=Rating.objects.filter(project=project_id)
    except Exception as e:
        raise Http404()
    #user single
    count=0
    for i in all:
        count+=i.usability
        count+=i.design
        count+=i.content

    if count>0:
        ave=round(count/3,1)
    else:
        ave=0


    if request.method=='POST':
        form=RatingsForm(request.POST)
        if form.is_valid():
            rate=form.save(commit=False)
            rate.user=request.user
            rate.project=project_id
            #review
            rate.save()
            return redirect('details',project_id)
    else:
        form=RatingsForm()

    
    votes=Rating.objects.filter(project=project_id)
    usability=[]
    design=[]
    content=[]

    for i in votes:
        usability.append(i.usability)
        design.append(i.design)
        content.append(i.content)
    if len(usability) > 0 or len(design)> 0 or len(content) >0:

        average_usa=round(sum(usability)/len(usability),1)
        average_des=round(sum(design)/len(design),1)
        average_con=round(sum(content)/len(content),1)

        averageRating=round((average_con+average_des+average_usa)/3,1)
    else:
        average_usa=0.0
        average_des=0.0
        average_con=0.0
        averageRating=0.0
    '''
    Restricting user to rate only once
    '''
    arr1=[]
    for use in votes:
        arr1.append(use.user_id)

    auth=arr1


    if request.method=='POST':
        review=ReviewsForm(request.POST)
        if review.is_valid():
            comment=review.save(commit=False)
            comment.user=request.user
            comment.pro_id=project_id
            comment.save()
            return redirect('details',project_id)
    else:
        review=ReviewsForm()

    try:
        user_comment=Comments.objects.filter(pro_id=project_id)
    except Exception as e:
        raise Http404()
    return render(request,'details.html',{'projects':projects,'form':form,'usability':average_usa,'design':average_des,'content':average_con,'average':averageRating,'auth':auth,'all':all,'ave':ave,'review':review,'comments':user_comment})


