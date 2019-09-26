from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from .forms import *
from django.shortcuts import get_object_or_404
import requests
from requests.auth import HTTPBasicAuth
import json


# Create your views here.

def login(request):
    if request.method=='POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
        return render('login')

#landing page - home page
def index(request):

    index_path = Project.objects.all()
    return render(request,'index.html',locals())




def getAccessToken(request):
    consumer_key = 'ZGWH5CJonGUS9C7eRzvkQGgzMJShHaDD'
    consumer_secret = 'fcobUM436AD9TwyB'
    api_URL = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'
    r = requests.get(api_URL, auth=HTTPBasicAuth(consumer_key, consumer_secret))
    mpesa_access_token = json.loads(r.text)
    validated_mpesa_access_token = mpesa_access_token['access_token']
    return HttpResponse(validated_mpesa_access_token)

