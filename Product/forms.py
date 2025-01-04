from django import forms
from .models import *

class ProductForm(forms.ModelForm):
    class Meta:
        model   =Product

        fields  ='__all__'



        

class orderform(forms.ModelForm):
    class Meta:
        model   = order

        fields  = ['Product_ref','Customer_ref','Product_ref','Order_date','Quantity']