from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from Product.models import Product
from .form import *


def loginpage(request):
    if request.method=="POST":
        print (request.POST)
        user_data=authenticate(username=request.POST['username'], password=request.POST['password'])
        print(user_data)
        if user_data is not None:
            login(request,user_data)
            return redirect('/Product/productlist/')
        else:
            msg={"error":"!Invalid Username And Password!"}
            return render(request,'login.html',msg)

    
    return render(request,"login.html")

def logoutpage(request):
    logout(request)
    return redirect("/")


def signup1(request):
    if request.method=="POST":
         
        usercheck=userdetails.objects.filter(username=request.POST['username'])

        if usercheck is not None :
            msg={"error":"Username already exists"}
            return render(request,'signup1.html',msg)
        else:
            newuser=userdetails(username=request.POST['username'],
                            first_name=request.POST['firstname'],
                            last_name=request.POST['lastname'],
                            Mobile_number=request.POST['mobilenumber'],
                            Address=request.POST['address'],
                            Age=request.POST['age'],
                            
                            )
        newuser.set_password(request.POST['password'])
        newuser.save()
        return redirect('/')

    return render(request,'signup1.html')