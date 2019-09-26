from django.conf.urls import url,include
from . import views
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    url(r'^payment', views.payment, name='payment'),

]