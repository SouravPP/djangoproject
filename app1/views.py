
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from .forms import LoginForm, RegisterForm,UpdateForm
from . models import Register
# Create your views here.
def hello(request):
    return HttpResponse("welcome to project3")

#rendering html pages
def index(request):
    return render(request,'index.html')

def signup(request):
    if request.method=='POST':
      form=RegisterForm(request.POST)
      if form.is_valid():
        name=form.cleaned_data['Name']
        age=form.cleaned_data['Age']
        place=form.cleaned_data['Place']
        email=form.cleaned_data['Email']
        password=form.cleaned_data['Password']
        confirmpassword=form.cleaned_data['ConfirmPassword']

        user=Register.objects.filter(Email=email).exists()

        if user:
            messages.warning(request,"Email already exist")
            return redirect('/signup')
        elif password!=confirmpassword:
            messages.warning(request,"password missmatch")
            return redirect('/signup')
        else:
            tab=Register(Name=name,Age=age,Place=place,Email=email,Password=password)   
            tab.save()
            messages.success(request,"data saved....")
            return redirect('/')

    else:
        form=RegisterForm()
    return render(request,'signup.html',{'form':form})          

def login(request):
    if request.method=='POST':
        form=LoginForm(request.POST)
        if form.is_valid():
            email=form.cleaned_data['Email']
            password=form.cleaned_data['Password']

            user=Register.objects.get(Email=email)

            if not user:
                messages.warning(request,"Email doesnot exist")
                return redirect('/login')

            elif password!=user.Password:
                messages.warning(request,"incorrect password")
                return redirect('/login')
            
            else:
                messages.success(request,"login successful")
                return redirect('/home/%s' % user.id)

    else:
        form=LoginForm()
    return render(request,'login.html',{'form':form})       
def home(request,id):
    user=Register.objects.get(id=id)
    return render(request,'home.html',{'user':user})

def display_table(request):
    users=Register.objects.all()
    return render(request,'display.html',{'users':users})


def update(request,id):
    user=Register.objects.get(id=id)
    if request.method=='POST':
      form=UpdateForm(request.POST or None, instance=user)
      if form.is_valid():
        name=form.cleaned_data['Name']
        age=form.cleaned_data['Age']
        place=form.cleaned_data['Place']
        email=form.cleaned_data['Email']
        form.save()
        messages.success(request,"data updated....")
        return redirect('/home/%s' % user.id)

    else:
        form=UpdateForm(instance=user)
    return render(request,'update.html',{'form':form,'user':user})    

def remove(request,id):
    user=Register.objects.get(id=id)
    user.delete()
    messages.success(request,"delete successfully...")
    return redirect('/display_table')      

    
