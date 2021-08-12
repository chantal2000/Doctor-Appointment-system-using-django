from django.core.checks import messages
from django.shortcuts import render

from django.shortcuts import render,redirect
from django.contrib.auth.models import User,Group
from .models import *
from django.contrib.auth import authenticate,logout,login

def homepage(request):
    return render(request,'index.htm')
def aboutpage(request):
    return render(request,'about.htm')
def signuppage(request):
    if request.method=="POST":
        username=request.POST['username']
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']
        myuser=User.objects.create_user(username,email,pass1)
        myuser.first_name=fname
        myuser.last_name=lname
        myuser.save()
        messages.success(request,"Your account has been successfully created")
        return redirect('signin')
    return render(request,'signup.htm')
def signin(request):
    return render(request,'signin.htm')
def signout(request):
    return render(request,'signout.htm')


def login_admin(request):
    error=""
    if request.method=="POST":
        u=request.POST['username']
        p=request.POST['password']
        user=authenticate(username=u,password=p)
        try:
            if user.is_staff:
                login(request,user)
                error="no"
            else:
                error="yes"
        except:
            error="yes"
    d={'error':error}
    return render(request,'adminLogin.htm',d)

def loginpage(request):
    error=""
    page=""
    if request.method=="POST":
        u=request.POST['email']
        p=request.POST['password']
        user=authenticate(request,username=u,password=p)
        try:
            if user is not None:
                login(request,user)
                error="no"
                g=request.user.groups.all()[0].name
                if g=='Doctor':
                    page='doctor'
                    d={'error':error,'page':page}
                    return render(request,'patienthome.htm',d)
                else:
                    error="yes"
        except Exception as o:
            error="yes"
    return render(request,'login.htm')
def adminhomepage(request):
    return render(request,'index.htm')
def adddoctorpage(request):
    return render(request,'.htm')
def viewdoctorpage(request):
    return render(request,'.htm')
def addreceptpage(request):
    return render(request,'.htm')
def viewreceptpage(request):
    return render(request,'.htm')
def viewappointpage(request):
    return render(request,'.htm')
def adminlogoutpage(request):
    return render(request,',htm')
def logoutpage(request):
    return render(request,'.htm')
def createAccount(request):
    error=""
    user="none"


