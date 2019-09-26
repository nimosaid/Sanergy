from django import forms
from .models import Customer
from django.contrib.auth.models import User

class RegisterCustomer(forms.ModelForm):
    class meta:
        model = Customer