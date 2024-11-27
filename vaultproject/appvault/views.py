from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib import messages
from .models import *
import os
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
    data=File.objects.filter(user=req.user)
    return render(req,'user/vaultuser.html',{'data':data})

def addfile(req,id):
    if req.method=='POST':
        user=User.objects.get(pk=id)
        name=req.POST['name']
        file=req.FILES['allfile']
        data=File.objects.create(user=user,name=name,files=file)
        data.save()
        return redirect(vault)
    else:
       return render(req,'user/addfile.html')

def f_delete(req,id):
    data=File.objects.get(pk=id)
    data.delete()
    return redirect(vault)