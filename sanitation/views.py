from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from django.shortcuts import get_object_or_404




#landing page - home page
def index(request):

    return render(request,'index.html')
# def welcome(request):
#     return HttpResponse('Welcome to the Moringa Tribune')



# def search_project(request):

#     if 'project' in request.GET and request.GET["project"]:
#         search_term = request.GET.get("project")
#         searched_project = Project.search_by_name(search_term)
#         message = f"{search_term}"

#         return render(request, 'search.html',locals())

#     else:
#         message = "You haven't searched for any term"
#         return render(request, 'search.html',locals())

