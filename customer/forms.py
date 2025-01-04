from django import forms
from .models import *

class customerform(forms.ModelForm):
    class Meta:
        model   =customer

        fields  ='__all__'