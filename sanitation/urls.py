<<<<<<< HEAD
=======

from django.conf import settings

>>>>>>> fe073c049c5c715e3eadcd570f01b2015244c0cc
from django.conf.urls import url,include
from . import views
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
<<<<<<< HEAD
=======
    url(r'^$',views.index, name="homePage"),
    url(r'^$',views.index, name="homePage")
   

from django.conf.urls import url,include
from . import views
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
>>>>>>> fe073c049c5c715e3eadcd570f01b2015244c0cc
    url(r'^payment', views.payment, name='payment'),
    url('access/token', views.getAccessToken, name='get_mpesa_access_token'),
    url('online/lipa', views.lipa_na_mpesa_online, name='lipa_na_mpesa'),

]
