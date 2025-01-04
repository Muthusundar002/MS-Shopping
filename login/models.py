from django.db import models
from Product.models import *
from django.contrib.auth.models import AbstractUser

# class signup(models.Model):
#     Username=models.CharField(max_length=20,null=True)
#     Password=models.CharField(max_length=20,null=True)
#     Full_name=models.CharField(max_length=20,null=True)
#     MObile_number=models.CharField(max_length=20,null=True)
#     Address=models.CharField(max_length=20,null=True)
#     Product_ref=models.ForeignKey(Product,on_delete=models.SET_NULL,null=True)

class userdetails(AbstractUser):
    Mobile_number=models.CharField(max_length=200,null=True)
    Address=models.CharField(max_length=200,null=True)
    Age=models.IntegerField(default=1,null=True)
