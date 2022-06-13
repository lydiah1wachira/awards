from django.shortcuts import render,redirect

# Create your views here.
def index(request):
  '''View function to display the index page and its data'''
  
  return render(request, 'index.html')
