from django.db import models
from customer.models import *

class Product(models.Model):
   

    Model_name   =models.CharField(max_length=200,null=True)

    Brand_name     =models.CharField(max_length=200,null=True)

    Price          =models.IntegerField(default=0)

    GST            =models.FloatField(default=0)

    Final_price    =models.IntegerField(default=0)  

    # Picture         =models.ImageField(null=True, upload_to='images/')  

    def __str__(self):
        return self.Model_name+" "+self.Brand_name
    

class order(models.Model):
   

    
    Customer_ref     =models.ForeignKey(customer,on_delete=models.SET_NULL,null=True)

    Product_ref      =models.ForeignKey(Product,on_delete=models.SET_NULL,null=True)


    Order_date       =models.DateField(null=True)

    Quantity         =models.IntegerField(default=0)

    Price         =models.IntegerField(default=0)

    GST         =models.FloatField(default=0)

    Final_price    =models.IntegerField(default=0)    

    
    

 
 
