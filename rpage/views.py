from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

def index(request):
  return render(request,'index.html')

def sign_up_page(request):
  template = loader.get_template('newuser.html')
  return HttpResponse(template.render())

def log_in_page(request):
  template = loader.get_template('login.html')
  return HttpResponse(template.render())





