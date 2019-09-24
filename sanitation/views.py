from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from .forms import *
from django.shortcuts import get_object_or_404


# Create your views here.
#first page - signup page
def signup(request):
    if request.method=='POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
        return redirect('login')

#landing page - home page
def index(request):

    index_path = Project.objects.all()
    return render(request,'index.html',locals())




# def search_project(request):

#     if 'project' in request.GET and request.GET["project"]:
#         search_term = request.GET.get("project")
#         searched_project = Project.search_by_name(search_term)
#         message = f"{search_term}"

#         return render(request, 'search.html',locals())

#     else:
#         message = "You haven't searched for any term"
#         return render(request, 'search.html',locals())

