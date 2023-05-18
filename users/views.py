from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from .models import Member

# Create your views here.
def register_user(request):
  print('request accepted')
  if request.method == 'POST':
    print('request arrived')
    username_value=request.POST['user_name']
    password_value=request.POST['password']
    phone_num_value=request.POST['phone_num']
    gender_value=request.POST['radio_option']
    
    user = Member.objects.create(username = username_value, password = password_value,  phone_num = phone_num_value, gender = gender_value)
    user.save();
    print(username_value)
    print('created')
    return render(request,'login.html',{'message': 'Update Success', })
  else:
    return render('newuser.html')
  
def check_user(request):
  print('request accepted')
  if request.method == 'POST':
    print('request arrived')
    username_input=request.POST['user_name']
    password_input=request.POST['password']
    incorrect_credentials=0

    if Member.objects.filter(username = username_input , password = password_input).exists():
      return render(request,'home.html',{'message': 'Login Success','data': Member.objects.filter(username=username_input)})
    else:
      incorrect_credentials = 1
      return render(request,'login.html', {'incorrect' : incorrect_credentials})
    
def home_page(request):
  #member = Member.objects.all()
  # template = loader.get_template('home.html')
  # context = {
  #   'Member': Member,
  # }
  # return render(request,'home.html',{'data':Member.objects.all()} )
  return render(request,'home.html', )
      
        