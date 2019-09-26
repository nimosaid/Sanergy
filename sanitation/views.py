from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from .forms import *
from django.shortcuts import get_object_or_404


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