from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.
def val_login(req):
    if 'user' in req.session:
        return redirect(vault)
    if req.method=='POST':
        uname=req.POST['uname']
        password=req.POST['password']
        user=authenticate(username=uname,password=password)
        if user:
            login(req,user)
            return redirect(vault)
        else:
            messages.warning(req,'Invaild username or password!!!')
            return redirect(val_login)
    else:
        return render(req,'login.html')
    
def val_logout(req):
    logout(req)
    req.session.flush()
    return redirect(val_login)
    
    
def register(req):
    if req.method=='POST':
        email=req.POST['email']
        uname=req.POST['uname']
        password=req.POST['password']
        try:
            data=User.objects.create_user(first_name=uname,email=email,username=email,password=password)
            data.save()
            return redirect(val_login)
        except:
            messages.warning(req,'Email Already Exists!!')
            return redirect(register)
    return render(req,'user/register.html')

def vault(req):
  return render(req,'user/vaultuser.html')

def addfile(req):
    return render(req,'user/addfile.html')