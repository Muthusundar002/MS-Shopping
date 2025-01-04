from django.db import models
from .models import *
from Product.models import *



class customer(models.Model):
    Full_name  =models.CharField(max_length=200,null=True)

    Mobile_number   =models.CharField(max_length=200,null=True)

    Address     =models.CharField(max_length=200,null=True)

    Age          =models.IntegerField(default=0)

    # Selected_course=models.ForeignKey(Product,on_delete=models.SET_NULL,null=True)     
    

    def __str__(self):
        return self.Full_name