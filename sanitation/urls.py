
from django.conf import settings

from django.conf.urls import url,include
from . import views

urlpatterns = [
    url(r'^$',views.index, name="homePage"),
    url(r'^$',views.index, name="homePage")
   

from django.conf.urls import url,include
from . import views
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    url(r'^payment', views.payment, name='payment'),
    url('access/token', views.getAccessToken, name='get_mpesa_access_token'),
    url('online/lipa', views.lipa_na_mpesa_online, name='lipa_na_mpesa'),

]
