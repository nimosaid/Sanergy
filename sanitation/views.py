from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from django.shortcuts import get_object_or_404




#landing page - home page
def index(request):

    return render(request,'index.html')

