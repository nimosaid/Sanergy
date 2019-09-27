"""sanergy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
<<<<<<< HEAD
from django.conf.urls import url,include

=======

import sanitation.urls
>>>>>>> fe073c049c5c715e3eadcd570f01b2015244c0cc
urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'',include('sanitation.urls')),
<<<<<<< HEAD

]
=======
]

from django.conf.urls import url,include

urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'',include('sanitation.urls')),

]

>>>>>>> fe073c049c5c715e3eadcd570f01b2015244c0cc
