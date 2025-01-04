from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required

@login_required(login_url='/')
def customerlist(request):
    data={"prolist":customer.objects.all()}
    return render(request,'customerlist.html',data)
def customeradd(request):
    data={"cusform":customerform}
    newdata=customerform(request.POST)
    if request.method == "POST":
        if newdata.is_valid():
            newdata.save()
        return redirect("/customer/customerlist/")
    return render(request,'customeradd.html',data)
def customerupdate(request,id):
    select_data=customer.objects.get(id=id)
    data={"cusform":customerform(instance=select_data)}

    if request.method == "POST":
        new_data=customerform(request.POST,instance=select_data)
        if new_data.is_valid():
            new_data.save()
            return redirect("/customer/customerlist")
    return render(request,"customeradd.html",data)

def customerdelete(request,id):
    selected_data=customer.objects.get(id=id)
    selected_data.delete()
    return redirect("/customer/customerlist/")
