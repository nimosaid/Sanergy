from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from .forms import *
from django.shortcuts import get_object_or_404
import requests
from requests.auth import HTTPBasicAuth
import json
from .mpesa_credentials import *
from django.views.decorators.csrf import csrf_exempt
from .models import *
from .forms import *

from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.

def login(request):
    if request.method=='POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
        return render('login')

#landing page - home page
def index(request):


    return render(request,'index.html',locals())


def payment(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            name=form.save(commit=False)
            phone_Number= form.save(commit=False)
            amount = form.save(commit=False)
            account= form.save(commit=False)
            payment.save()
            return redirect(hood)
    else:
        form = PaymentForm()
    return render(request,'payment.html',locals())

def toilet(request):


    this_user_id_number = User.objects.all()
    if request.method == 'POST':

        form = ToiletForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            account_number=form.save(commit=False)
            toilet_tag=form.save(commit=False) 
            # toilet.save()
            return redirect(index)
    else:
        form = ToiletForm()
    return render(request,'toilet.html',locals())            
   



def getAccessToken(request):
    consumer_key = 'cHnkwYIgBbrxlgBoneczmIJFXVm0oHky'
    consumer_secret = '2nHEyWSD4VjpNh2g'
    api_URL = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'
    r = requests.get(api_URL, auth=HTTPBasicAuth(consumer_key, consumer_secret))
    mpesa_access_token = json.loads(r.text)
    validated_mpesa_access_token = mpesa_access_token['access_token']
    return HttpResponse(validated_mpesa_access_token)
def lipa_na_mpesa_online(request):
    access_token = MpesaAccessToken.validated_mpesa_access_token
    api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
    headers = {"Authorization": "Bearer %s" % access_token}
    request = {
        "BusinessShortCode": LipanaMpesaPpassword.Business_short_code,
        "Password": LipanaMpesaPpassword.decode_password,
        "Timestamp": LipanaMpesaPpassword.lipa_time,
        "TransactionType": "CustomerPayBillOnline",
        "Amount": 1,
        "PartyA": 254717654230,  # replace with your phone number to get stk push
        "PartyB": LipanaMpesaPpassword.Business_short_code,
        "PhoneNumber": 254717654230,  # replace with your phone number to get stk push
        "CallBackURL": "https://sandbox.safaricom.co.ke/mpesa/",
        "AccountReference": "Obindi",
        "TransactionDesc": "Testing stk push"
    }
    response = requests.post(api_url, json=request, headers=headers)
    return HttpResponse('success')    

#consuming mpesa api biils

def bills(request):
    url = 'https://sandbox.safaricom.co.ke/mpesa/?api_key=ZGWH5CJonGUS9C7eRzvkQGgzMJShHaDD'
    response = requests.get(url.format()).json()
    details = []
    for detail in details:
        amount = detail.get('amount')
        phone_number = detail.get('phone_number')
        reference = detail.get('reference')
        return HttpResponse(response.text)

    return render(request, 'bills.html', {'details': details})


def search_results(request):

    if 'article' in request.GET and request.GET["phone"]:
        search_term = request.GET.get("phone")
        searched_phone = Phone.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'data/search.html',{"message":message,"phone": searched_phones})

    else:
        message = "You haven't searched for any term"
        return render(request, 'data/search.html',{"message":message})
