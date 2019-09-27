from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from .forms import *
from django.shortcuts import get_object_or_404


# Create your views here.

def login(request):
    if request.method=='POST':
        form = RegisterCustomer(request.POST)

        if form.is_valid():
            form.save()
        return redirect('login')

#landing page - home page
def index(request):

    # index_path = Project.objects.all()
    return render(request,'index.html',locals())
