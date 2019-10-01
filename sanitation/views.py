from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
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


#landing page - home page
def index(request):

    return render(request,'index.html')

    index_path = Project.objects.all()
    return render(request,'index.html',locals())



def payment(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            phone_Number = form.cleaned_data['phone_Number']
            amount = form.cleaned_data['amount']
            # form.save(commit=False)
            # payment.save()
            lipa_na_mpesa_online(phone_Number, amount)
            return redirect(lipa_na_mpesa_online)
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
    consumer_key = 'ZGWH5CJonGUS9C7eRzvkQGgzMJShHaDD'
    consumer_secret = 'fcobUM436AD9TwyB'
    api_URL = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'
    r = requests.get(api_URL, auth=HTTPBasicAuth(consumer_key, consumer_secret))
    mpesa_access_token = json.loads(r.text)
    validated_mpesa_access_token = mpesa_access_token['access_token']
    return HttpResponse(validated_mpesa_access_token)


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
        "CallBackURL": "https://sandbox.safaricom.co.ke/mpesa/",
        "AccountReference": "Obindi",
        "TransactionDesc": "Testing stk push"
    }
    response = requests.post(api_url, json=request, headers=headers)   



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
    mpesa_payment = json.loads(mpesa_body)
    payment = MpesaPayment(
        first_name=mpesa_payment['FirstName'],
        last_name=mpesa_payment['LastName'],
        middle_name=mpesa_payment['MiddleName'],
        description=mpesa_payment['TransID'],
        phone_number=mpesa_payment['MSISDN'],
        amount=mpesa_payment['TransAmount'],
        reference=mpesa_payment['BillRefNumber'],
        organization_balance=mpesa_payment['OrgAccountBalance'],
        type=mpesa_payment['TransactionType'],
    )
    payment.save()
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

        

    url = 'https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest?api_key=ZGWH5CJonGUS9C7eRzvkQGgzMJShHaDD'
	r = requests.get(url.format()).json()
	movie_list = r['results']
	print(movie_list)
	movie_results = []
	for movie_item in movie_list:
		id = movie_item.get('id')
		title = movie_item.get('original_title')
		overview = movie_item.get('overview')
		image = movie_item.get('poster_path')
		rating = movie_item.get('vote_average')
		vote_count = movie_item.get('vote_count'),
		age = movie_item.get('genre_ids[3]')

		if image:
			movie_object = Movie(id,title,overview,image,rating,vote_count,age)
			movie_results.append(movie_object)
			
	return render(request, "home.html", {"allmovies": movie_results})

