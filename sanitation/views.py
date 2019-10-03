from django.shortcuts import render,redirect
from django.http import HttpResponse, JsonResponse
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
from mpesa_api.core.mpesa import Mpesa
from .serializer import *
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.decorators import login_required

# Create your views here.

def login(request):
    if request.method=='POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
        return render('login')


from mpesa_api.core.mpesa import Mpesa
from .serializer import *
from rest_framework.response import Response
from rest_framework.views import APIView

      

#landing page - home page
def index(request):


    return render(request,'index.html',locals())


@login_required(login_url='/accounts/login/')
def my_profile(request):
    current_user=request.user
    profile =Profile.objects.get(username=current_user)
    return render(request,'profile/user_profile.html',{"profile":profile})


@login_required(login_url='/accounts/login/')
def user_profile(request,username):
    user = User.objects.get(username=username)
    profile =Profile.objects.get(username=user)

@login_required(login_url='/accounts/login/')
def create_profile(request):
    current_user=request.user
    if request.method=="POST":
        form =ProfileForm(request.POST,request.FILES)
        if form.is_valid():
            profile = form.save(commit = False)
            profile.username = current_user
            profile.save()
        return HttpResponseRedirect('/')
    else:
        form = ProfileForm()
        return render(request,'profile/profile_form.html',{"form":form})
    

@login_required(login_url='/accounts/login/')
def update_profile(request):
    current_user=request.user
    if request.method=="POST":
        instance = Profile.objects.get(username=current_user)
        form =ProfileForm(request.POST,request.FILES,instance=instance)
        if form.is_valid():
            profile = form.save(commit = False)
            profile.username = current_user
            profile.save()

        return redirect('index')

    elif Profile.objects.get(username=current_user):
        profile = Profile.objects.get(username=current_user)
        form = ProfileForm(instance=profile)
    else:
        form = ProfileForm()

    return render(request,'profile/update_profile.html',{"form":form})

# def login(request):
#     if request.method=='POST':
#         form = UserCreationForm(request.POST)

#         if form.is_valid():
#             form.save()
#         return render('login')



def payment(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()

            phone_Number = form.cleaned_data['phone_Number']
            amount = form.cleaned_data['amount']
            lipa_na_mpesa_online(phone_Number, amount)
            return redirect('bills')

    else:
        form = PaymentForm()
    return render(request,'payment.html',locals())

def toilet(request):


    this_user_id_number = User.objects.all()
    if request.method == 'POST':

        form = ToiletForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            phone_Number = form.cleaned_data['phone_Number']
            amount = form.cleaned_data['amount']
            # form.save(commit=False)
            # payment.save()
            lipa_na_mpesa_online(phone_Number, amount)
            return redirect('bills')
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

def lipa_na_mpesa_online(phone, amount):

    access_token = MpesaAccessToken.validated_mpesa_access_token
    api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
    headers = {"Authorization": "Bearer %s" % access_token}
    request = {
        "BusinessShortCode": LipanaMpesaPpassword.Business_short_code,
        "Password": LipanaMpesaPpassword.decode_password,
        "Timestamp": LipanaMpesaPpassword.lipa_time,
        "TransactionType": "CustomerPayBillOnline",
        "Amount": amount,
        "PartyA": phone,  # replace with your phone number to get stk push
        "PartyB": LipanaMpesaPpassword.Business_short_code,
        "PhoneNumber": phone,  # replace with your phone number to get stk push
        "CallBackURL": "https://0e070bc3.ngrok.io/confirmation/",
        "AccountReference": "Obindi",
        "TransactionDesc": "Testing stk push"
    }

    response = requests.post(api_url, json=request, headers=headers)
    return HttpResponse('success')    

    response = requests.post(api_url, json=request, headers=headers)   
    if response.status_code==200:
        data = response.json()
        if 'ResponseCode' in data.keys():
            if data['ResponseCode']==0:
                merchant_id = data['MerchantRequestID']
        pass
    merchant_id = response
    print(response.json())



@csrf_exempt
def register_urls(request):
    access_token = MpesaAccessToken.validated_mpesa_access_token
    api_url = "https://sandbox.safaricom.co.ke/mpesa/c2b/v1/registerurl"
    headers = {"Authorization": "Bearer %s" % access_token}
    options = {"ShortCode": LipanaMpesaPpassword.Business_short_code,
               "ResponseType": "Completed",
               "ConfirmationURL": "http://127.0.0.1:8000/api/v1/c2b/confirmation",
               "ValidationURL": "http://127.0.0.1:8000/api/v1/c2b/validation"}
    response = requests.post(api_url, json=options, headers=headers)
    return HttpResponse(response.text)
@csrf_exempt
def call_back(request):
    pass
@csrf_exempt
def validation(request):
    context = {
        "ResultCode": 0,
        "ResultDesc": "Accepted"
    }
    return JsonResponse(dict(context))
@csrf_exempt
def confirmation(request):
    mpesa_body =request.body.decode('utf-8')
    try:
        mpesa_payment = json.loads(mpesa_body)
    except Exception as e:
        print(e)
        context = {
            "ResultCode": 1,
            "ResultDesc": "Accepted"
        }
        return JsonResponse(dict(context)) 
    print(mpesa_payment) 
    if mpesa_payment['Body']['stkCallback']['ResultCode']==0:
        mpesa_payment = mpesa_payment['Body']['stkCallback']['CallbackMetadata']['Item']
        print(mpesa_payment)
        # payment = MpesaPayment(
        #     first_name=mpesa_payment['FirstName'],
        #     last_name=mpesa_payment['LastName'],
        #     middle_name=mpesa_payment['MiddleName'],
        #     description=mpesa_payment['TransID'],
        #     phone_number=mpesa_payment[4]['Value'],
        #     amount=mpesa_payment[0]['Value'],
        #     reference=mpesa_payment[1]['Value'],
        #     organization_balance=mpesa_payment['OrgAccountBalance'],
        #     type=mpesa_payment['TransactionType'],
        # )
        # payment.save()
        b = Bills(
           phone_number=mpesa_payment[4]['Value'],
           reference=mpesa_payment[1]['Value'],
           amount=mpesa_payment[0]['Value']
        ) 
        b.save()
        context = {
            "ResultCode": 0,
            "ResultDesc": "Accepted"
        }
        return JsonResponse(dict(context))    



class PaymentList(APIView):
    def get(self, request, format=None):
        all_mpesapayment = MpesaPayment.objects.all()
        serializers = MpesaPaymentSerializer(all_mpesapayment   , many=True)
        return Response(serializers.data)

        

   

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

    bills=Bills.objects.all()

    return render(request, 'bills.html', {'details': details})

