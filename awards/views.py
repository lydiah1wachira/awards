from django.shortcuts import render,redirect
from .models import Profile,Project
from django.http import HttpResponse,Http404,HttpResponseRedirect,JsonResponse

# Create your views here.
def index(request):
  '''View function to display the index page and its data'''
  
  try:
    projects = Project.objects.all()
  except Exception as e :
    raise  Http404()
      
  return render(request, 'index.html', {"projects":projects})
