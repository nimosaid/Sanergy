from django import forms
from.models import *



class PaymentForm(forms.ModelForm):
    class Meta:
        model  = Payment
        fields = ['name','account','phone_Number','amount']
