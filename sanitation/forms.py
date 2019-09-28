from django import forms
from.models import *
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction




class PaymentForm(forms.ModelForm):
    class Meta:
        model  = Payment
        fields = ['name','account','phone_Number','amount']

  