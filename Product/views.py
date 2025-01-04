from django.shortcuts import render,redirect
# from django.http import HttpResponse
from .models import *
from .forms import *
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin


def index(request):
   
    data={"user1":[{"Name":"Muthu","Loc":"Tuty","Score":90},
                  {"Name":"Perumal","Loc":"Kochadai","Score":80},
                  {"Name":"Karthi","Loc":"Kvp","Score":70},
                  {"Name":"Ela","Loc":"Ellis nagar","Score":60}
                  ]
    }
    return render(request,'index.html',data)

def about(request):
    return render(request,'about.html')


class productaddView(LoginRequiredMixin,View):
     login_url='/'
     def get(self,request):
          
      data={"proform":ProductForm}
      return render(request,'productadd.html',data)
     

     def post(self,request):
          newdata=ProductForm(request.POST,request.FILES)
          if request.method == "POST":
            if newdata.is_valid():
                newdata.save()
                return redirect("/Product/productlist/")
            
class productlistView(LoginRequiredMixin,View):
    login_url='/'
    def get(self,request):
         data={"prolist":Product.objects.all()}
         return render(request,'productlist.html',data)
    
class productupdateView(LoginRequiredMixin,View):
    login_url='/'
    def get(self,request,id):
        select_data=Product.objects.get(id=id)  
        data={"proform":ProductForm(instance=select_data)}
        return render(request,"productadd.html",data)
    def post(self,request,id):
                 select_data=Product.objects.get(id=id)
                 new_data=ProductForm(request.POST,instance=select_data)
                 if new_data.is_valid():
                    new_data.save()
                    return redirect("/Product/productlist/")
                 
class productdeleteView(LoginRequiredMixin,View):
     login_url='/'
     def get(self,request,id):
          selected_data=Product.objects.get(id=id)
          selected_data.delete()
          return redirect("/Product/productlist/")



def orderadd(request):
    data={"proform":orderform}
    
    if request.method == "POST":

            sp=Product.objects.get( id=request.POST['Product_ref'])

            pro_price=float(request.POST['Quantity'])*sp.Price
            pro_GST=  (pro_price * sp.GST)/100
            pro_FP=pro_price+pro_GST
            
            new_order=order(
                  

                  Customer_ref_id   = request.POST['Customer_ref'],

                   Product_ref_id   = request.POST['Product_ref'],

                  Order_date        = request.POST['Order_date'],

                  Quantity          = request.POST['Quantity'],

                  Price             = pro_price,

                  GST               = pro_GST,

                  Final_price       = pro_FP
                  )

            new_order.save()
            return redirect("/Product/orderlist/")
    return render(request,'orderadd.html',data)

def orderlist(request):

    data={"orderlist":order.objects.all()}
    
    return render(request,'orderlist.html',data)
def orderupdate(request,id):
    select_data=order.objects.get(id=id)
    data={"proform":orderform(instance=select_data)}

    if request.method == "POST":
            sp=Product.objects.get( id=request.POST['Product_ref'])

            pro_price=float(request.POST['Quantity'])*sp.Price
            pro_GST=  (pro_price * sp.GST)/100
            pro_FP=pro_price+pro_GST
            updated_row=order.objects.filter(id=id)
            updated_row.update( 

                  Customer_ref_id   = request.POST['Customer_ref'],

                  Product_ref_id   = request.POST['Product_ref'],

                  Order_date        = request.POST['Order_date'],

                  Quantity          = request.POST['Quantity'],

                  Price             = pro_price,

                  GST               = pro_GST,

                  Final_price       = pro_FP)
            
        
            return redirect("/Product/orderlist")
    return render(request,"orderadd.html",data)

def orderdelete(request,id):
    selected_data=order.objects.get(id=id)
    selected_data.delete()
    return redirect("/Product/orderlist/")
     
          
                

# def productlist(request):
#     data={"prolist":Product.objects.all()}
#     return render(request,'productlist.html',data)

# def productadd(request):
#     data={"proform":ProductForm}
#     newdata=ProductForm(request.POST,request.Files)
#     if request.method == "POST":
#         if newdata.is_valid():
#             newdata.save()
#         return redirect("/Product/productlist/")
#     return render(request,'productadd.html',data)

# def productupdate(request,id):
#     select_data=Product.objects.get(id=id)  
#     data={"proform":ProductForm(instance=select_data)}

#     if request.method == "POST":
#         new_data=ProductForm(request.POST,instance=select_data)
#         if new_data.is_valid():
#             new_data.save()
#             return redirect("/Product/productlist")
#     return render(request,"productadd.html",data)

# def productdelete(request,id):
#     selected_data=Product.objects.get(id=id)
#     selected_data.delete()
#     return redirect("/Product/productlist/")


            
     